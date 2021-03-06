import aiofiles
import asyncio
import logging
import re
import xml.etree.ElementTree as ElementTree
import concurrent.futures

from ..actions import actions
from ..manual import manual
from .. import braille
from . import book_file

log = logging.getLogger(__name__)

FORM_FEED = re.compile('\f')


async def init(book):
    if book.filename == manual.filename:
        return book

    log.debug('initialiazing {}'.format(book.filename))

    async with aiofiles.open(book.filename) as f:
        file_contents = await f.read()
    if len(file_contents) == 0:
        raise BookFileError('File is empty: {}'.format(book.filename))

    return book._replace(file_contents=file_contents, pages=tuple())

NS = {'pef': 'http://www.daisy.org/ns/2008/pef'}


def read_pages(book):
    if book.filename == manual.filename:
        return book
    if book.load_state == book_file.LoadState.DONE:
        return book
    log.debug('reading pages {}'.format(book.filename))
    pages = []
    if book.ext == '.brf':
        page = []
        for line in book.file_contents.splitlines():
            if FORM_FEED.match(line):
                # pad up to the next page
                while len(page) < book.height:
                    page.append('')
                if line == '\f':
                    continue
                else:
                    line = line.replace('\f', '')
            if len(page) == book.height:
                pages.append(tuple(page))
                page = []
            page.append(braille.from_ascii(line))
        if len(page) > 0:
            # pad up to the end
            while len(page) < book.height:
                page.append(tuple())
            pages.append(tuple(page))
    elif book.ext == '.pef':
        xml_doc = ElementTree.fromstring(book.file_contents)
        xml_pages = xml_doc.findall('.//pef:page', NS)
        lines = []
        for page in xml_pages:
            for row in page.findall('.//pef:row', NS):
                line = ''.join(row.itertext()).rstrip()
                lines.append(braille.from_unicode(line))
        for i in range(len(lines))[::book.height]:
            page = lines[i:i + book.height]
            # pad up to the end
            while len(page) < book.height:
                page.append(tuple())
            pages.append(tuple(page))
    else:
        raise BookFileError(
            'Unexpected extension: {}'.format(book.ext))
    bookmarks = book.bookmarks
    if len(pages) > 1:
        # add an end-of-book bookmark
        bookmarks += (len(pages) - 1,)
    return book._replace(pages=tuple(pages),
                         load_state=book_file.LoadState.DONE,
                         bookmarks=bookmarks)


async def get_page_data(book, store, page_number=None):
    if page_number is None:
        page_number = book.page_number
    if len(book.pages) == 0:
        while book.load_state == book_file.LoadState.LOADING:
            await asyncio.sleep(1)
            # accessing store.state will get a fresh state
            book = store.state['app']['user']['books'][book.filename]
        else:
            await store.dispatch(actions.set_book_loading(book))
            book = read_pages(book)
            await store.dispatch(actions.add_or_replace(book))

    if page_number >= len(book.pages):
        return book.pages[len(book.pages) - 1]

    return book.pages[page_number]

# in seconds
LOAD_BOOKS_TIMEOUT = 9 * 60


async def fully_load_books(store):
    state = store.state['app']
    if state['load_books'] == 'start':
        await store.dispatch(actions.load_books('loading'))
        books = state['user']['books']
        log.info('loading {} books'.format(len(books)))
        aborted = False
        futures = []

        with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:

            # gather futures for reading books
            for filename in books:
                book = books[filename]
                if book.load_state == book_file.LoadState.INITIAL:
                    await store.dispatch(actions.set_book_loading(book))
                    future = executor.submit(read_pages, book)
                    futures.append(future)

            # check if the futures are completed but don't hog this thread to wait
            # for that, asyncio.sleep instead
            await asyncio.sleep(2)
            try:
                for future in concurrent.futures.as_completed(futures, timeout=LOAD_BOOKS_TIMEOUT):
                    # accessing store.state will get a fresh state
                    if store.state['app']['load_books'] == 'cancel':
                        aborted = True
                        stop_process_pool(executor)
                        break
                    book = future.result(timeout=LOAD_BOOKS_TIMEOUT)
                    await store.dispatch(actions.add_or_replace(book))
                    await asyncio.sleep(0.1)
            except concurrent.futures.TimeoutError:
                log.warning('loading books timed out')
                aborted = True
                stop_process_pool(executor)

            await store.dispatch(actions.load_books(False))
            if aborted:
                log.info('loading books aborted')
            else:
                log.info('loading books done')


def stop_process_pool(executor):
    for pid, process in executor._processes.items():
        process.terminate()
    executor.shutdown()


class BookFileError(Exception):
    pass

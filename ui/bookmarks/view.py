from ..braille import from_ascii, format_title, to_ueb_number
from ..book.handlers import get_page_data


def render_help_menu(width, height):
    data = []

    data.append(from_ascii('Add a bookmark by pressing button #e'))
    data.append(from_ascii('while in a book. Bookmarks are listed'))
    data.append(from_ascii('here in the bookmark menu. Each bookmark'))
    data.append(from_ascii('starts with the Canute page number based'))
    data.append(from_ascii('on its #i line page. Go to the page by'))
    data.append(from_ascii('selecting a bookmark by pressing one of'))
    data.append(from_ascii('the side buttons. Holding the button'))
    data.append(from_ascii('down will delete the bookmark.'))

    # pad page with empty rows
    while len(data) < height:
        data.append(tuple())

    return tuple(data)


async def render(width, height, state, store):
    help_menu = state['help_menu']['visible']
    if help_menu:
        return render_help_menu(width, height)

    book = state['user']['books'][state['user']['current_book']]
    page = state['bookmarks_menu']['page']

    line_n = page * (height - 1)
    bookmarks = book.bookmarks[line_n:line_n + (height - 1)]

    max_pages = (len(book.bookmarks) - 1) // (height - 1)
    title = format_title(
        'bookmarks: {}'.format(book.title),
        width, page, max_pages)
    data = [title]

    end_inserted = False

    for bm in bookmarks:
        if bm == 0:
            data.append(from_ascii('start of book'))
        elif bm == book.max_pages:
            end_inserted = True
            data.append(from_ascii('end of book'))
        elif bm == 'deleted':
            data.append(tuple())
        else:
            lines = await get_page_data(book, store, page_number=bm)
            line = lines[0]
            n = from_ascii(to_ueb_number(bm + 1) + ' ')
            data.append(n + tuple(line))

    if not end_inserted:
        data.append(from_ascii('end of book'))

    # pad page with empty rows
    while len(data) < height:
        data.append(tuple())

    return tuple(data)

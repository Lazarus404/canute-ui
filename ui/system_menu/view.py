from ..braille import from_ascii, format_title
from .system_menu import menu_titles


def render_help_menu(width, height, page):
    data = [
        'Configure your preference on the sorting',
        'order of books in the library and',
        'bookmarks through the menu options. To',
        'shutdown the Canute safely, select the',
        'shutdown option and wait for #cj',
        'seconds before unplugging it.',
    ]

    data = [from_ascii(line) for line in data]

    while len(data) < height:
        data.append(tuple())

    return tuple(data)


def render(width, height, state):
    if state['help_menu']['visible']:
        return render_help_menu(width, height, state['help_menu']['page'])

    page = state['system_menu']['page']
    data = list(menu_titles)
    # subtract title from page height
    data_height = height - 1
    max_pages = 0
    title = format_title('system menu', width, page, max_pages)
    n = page * data_height
    data = data[n: n + data_height]
    # pad page with empty rows
    while len(data) < data_height:
        data += (tuple(),)
    return tuple([title]) + tuple(data)

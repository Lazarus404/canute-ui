from ..actions import actions

book_buttons = {
    'single': {
        '2': actions.enter_go_to_page(),
        '5': actions.insert_bookmark(),
        '6': actions.go_to_bookmarks_menu(),
        '8': actions.go_to_system_menu(),
        '9': actions.go_to_library(),
        '>': actions.next_page(),
        '<': actions.previous_page(),
        'L': actions.toggle_home_menu(),
        'R': actions.toggle_help_menu(),
    },
    'long': {
        '2': actions.enter_go_to_page(),
        '5': actions.insert_bookmark(),
        '6': actions.go_to_bookmarks_menu(),
        '8': actions.go_to_system_menu(),
        '9': actions.go_to_library(),
        '<': actions.skip_pages(-5),
        '>': actions.skip_pages(5),
        'L': actions.toggle_home_menu(),
        'R': actions.toggle_help_menu(),
        'X': actions.reset_display('start')
    },
}

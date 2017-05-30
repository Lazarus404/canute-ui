from frozendict import frozendict
from functools import partial
import pickle
import logging
log = logging.getLogger(__name__)

import utility
import menu


initial_state = utility.freeze({
    'app': {
        'location' : 'library',
        'library'  : {'data': [], 'page': 0},
    },
    'menu'     : {
        'data': [utility.pad_line(40, line) for line in menu.menu_titles_braille],
        'page': 0
    },
    'books'             : [],
    'replacing_library' : False,
    'backing_up_log'    : False,
    'shutting_down'     : False,
    'halt_ui'           : False,
    'warming_up'        : False,
    'resetting_display' : False,
    'update_ui'         : False,
    'display'           : {'width': 40, 'height': 9},
})

state_file = 'state.pkl'

def read(state_file = state_file):
    log.debug('reading initial state from %s' % state_file)
    try:
        with open(state_file) as fh:
            state = pickle.load(fh)
            return state
    except:
        log.debug('error reading state file, using hard-coded initial state')
        return initial_state


def write(state):
    log.debug('writing state file')
    write_state  = utility.unfreeze(state)
    write_state['app']['library'] = state['app']['library'].copy(page = 0)
    location = state['app']['location']
    if location == 'menu':
        location = 'library'
    write_state['app']['location']   = location
    write_state['backing_up_log']    = False
    write_state['replacing_library'] = False
    write_state['resetting_display'] = False
    write_state['warming_up']        = False
    write_state['shutting_down']     = False
    with open(state_file, 'w') as fh:
        pickle.dump(utility.freeze(write_state), fh)

if __name__ == '__main__':
    import os
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    print(read(state_file = dir_path + "/state.pkl")['update_ui'])

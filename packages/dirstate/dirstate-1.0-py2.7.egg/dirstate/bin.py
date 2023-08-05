import os
import sys
import json
from dirstate.utils import initialize
from dirstate.state import save_state, get_states, set_state


def run():
    initialize()

    path = os.getcwd()

    if sys.argv[1] == 'log':
        states = get_states(path)

        for state in states:
            del state['file']
            print(json.dumps(state, indent=4, sort_keys=True, default=str))

    elif sys.argv[1] == 'save':
        print('Saving current state...')
        state_id = save_state(path)
        print('State was saved: {}'.format(state_id))
    elif sys.argv[1] == 'set':
        print('Changing state...')
        timestamp = set_state(path, sys.argv[2])
        print('State set: {}'.format(timestamp))

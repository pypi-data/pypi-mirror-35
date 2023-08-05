import os
import glob
import ntpath
import shutil
from dirstate.utils import compress, new_state_id, parse_state_id, decompress
from dirstate.constants import DIRECTORY


def get_states(directory):
    return sorted(
        filter(
            lambda x: x['directory'] == directory,
            [
                dict(
                    parse_state_id(ntpath.basename(fname.split('.tar.gz')[0])),
                    **dict(file=fname)
                )
                for fname in glob.glob(os.path.join(DIRECTORY, '*.tar.gz'))
            ]
        ),
        key=lambda x: x['date']
    )


def save_state(directory):
    state_id = new_state_id(directory)

    compress(
        os.path.join(DIRECTORY, state_id),
        directory
    )

    return state_id


def set_state(directory, timestamp):
    state = None

    states = filter(
        lambda x: x['timestamp'] == timestamp,
        get_states(directory)
    )

    if not states:
        return False
    else:
        state = states[0]

    shutil.rmtree(directory)
    decompress(state['file'], directory)

    return timestamp

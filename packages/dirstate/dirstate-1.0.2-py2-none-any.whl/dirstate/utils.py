import tarfile
import datetime
import base64
import os
from dirstate.constants import STATE_DELIMETER, DIRECTORY


def initialize():
    if not os.path.isdir(DIRECTORY):
        os.mkdir(DIRECTORY)


def compress(filename, directory):
    with tarfile.open(filename + '.tar.gz', mode='w:gz') as archive:
        archive.add(
            directory,
            recursive=True,
            arcname=''
        )
    archive.close()

    return archive


def decompress(filename, directory):
    tar = tarfile.open(filename, 'r:gz')
    tar.extractall(path=directory)
    tar.close()


def new_timestamp():
    return int(datetime.datetime.now().strftime('%s'))


def new_state_id(directory):
    return base64.b64encode(
        '{}{}{}'.format(directory, STATE_DELIMETER, new_timestamp())
    )


def parse_state_id(state_id):
    parts = base64.b64decode(state_id).split(STATE_DELIMETER)

    return {
        'directory': parts[0],
        'timestamp': parts[1],
        'date': datetime.datetime.fromtimestamp(float(parts[1]))
    }


def to_mb(value):
    return value / (1024*1024.0)

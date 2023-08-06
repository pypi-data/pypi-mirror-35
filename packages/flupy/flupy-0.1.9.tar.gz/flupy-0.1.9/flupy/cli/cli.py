import importlib
import sys

from signal import signal, SIGPIPE, SIG_DFL

from flupy import flu
from flupy.cli.utils import LazyObject


lazy_modules = ['json', 'os', 'csv', 're', 'math', 'random', 'statistics']
for module in lazy_modules:
    locals()[module] = LazyObject(load=lambda : importlib.import_module('os'),
                                  ctx=globals(),
                                  name='os')

def read_file(filename):
    with open(filename, 'r') as f:
        yield from f


import argparse
parser = argparse.ArgumentParser(description='flupy: a fluent interface for python')
parser.add_argument('command', help='flupy command to execute on input')
parser.add_argument('-f', '--file', help='path to input file')


def main():
    args = parser.parse_args()

    _command = args.command
    _file = args.file

    if _file:
        _ = flu(read_file(_file)).map(str.rstrip)
    else: 
        # Do not raise exception for Broken Pipe
        signal(SIGPIPE, SIG_DFL)
        _ = flu(sys.stdin).map(str.rstrip)

    pipeline = eval(_command)

    if hasattr(pipeline, '__iter__'):
        for r in pipeline:
            sys.stdout.write(str(r) + '\n')
    else:
        sys.stdout.write(str(pipeline) + '\n')

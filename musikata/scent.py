from subprocess import call
from sniffer.api import runnable
import sys

@runnable
def execute_tests(*args):
    fn = [ 'python', 'manage.py', 'test' ]

    for i in range(len(sys.argv)):
        if sys.argv[i].startswith('-x'):
            sys.argv[i] = sys.argv[i][2:]
    
    fn += sys.argv[1:]
    return call(fn) == 0

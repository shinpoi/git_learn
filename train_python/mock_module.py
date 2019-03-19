# python3

"""
# python2
from mock import patch, mock_open
import __builtin__
"""

from unittest.mock import patch, mock_open
import builtins as __builtin__
import subprocess
import t2

"""
# t2.py
def run():
    with open('foo', 'r') as f:
        print(f.read())
    
    with open('foo.sql', 'r') as f:
        print(f.read())

if __name__ == '__main__':
    run()

# echo 'this is foo' > foo
# echo 'this is foo.sql' > foo.sql
"""

bi_open = __builtin__.open

class LogsTestOpen(object):
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        if filename.endswith('.sql'):
            self._open = mock_open(read_data='this is mock_open()')
        else:
            self._open = bi_open

    def __enter__(self):
        self.fd = self._open(self.filename, self.mode)
        return self.fd

    def __exit__(self, type, value, traceback):
        self.fd.close()


with patch('builtins.open', LogsTestOpen, create=True):
    t2.run()
    print(subprocess.check_output(['python3', 't2.py']).decode('utf-8'))

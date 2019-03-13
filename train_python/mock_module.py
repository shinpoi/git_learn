# python2

from mock import patch, mock_open
import __builtin__

"""
# python3: 
from unittest.mock import patch, mock_open
import builtins as __builtin__
"""

class LogsTestOpen(object):
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        if filename.endswith('.sql'):
            self._open = mock_open(read_data='this is mock_open()')
        else:
            self._open = __builtin__.open

    def __enter__(self):
        self.fd = self._open(self.filename, self.mode)
        return self.fd

    def __exit__(self, type, value, traceback):
        self.fd.close()


with patch('__main__.open', LogsTestOpen, create=True):
    with open('foo', 'r') as f:
        print(f.read())
    
    with open('foo.sql', 'r') as f:
        print(f.read())

    """
    import hoge
    hoge.run() <-- if open() used, that open() will not get patch
    """

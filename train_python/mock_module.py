try:
    from unittest.mock import patch, mock_open  # python3
except ImportError:
    from mock import patch, mock_open  # python2

import builtins as __builtin__
import builtins
import t2

"""
# t2.py
def run():
    with open('foo', 'r') as f:
        print(f.read())
    
    with open('foo.sql', 'r') as f:
        print(f.read())

# echo 'this is foo' > foo
# echo 'this is foo.sql' > foo.sql
"""

bi_open = __builtin__.open

def LogsTestOpen(filename, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True):
    if filename.endswith('.sql'):
        _open = mock_open(read_data='this is mock_open()')
    else:
        _open = bi_open

    return _open(filename, mode, buffering, encoding, errors, newline, closefd)

with patch('builtins.open', LogsTestOpen, create=True):
    t2.run()

"""
$ python2.7 t.py 
this is foo

this is foo.sql

$ python3.6 t.py 
this is foo

this is mock_open()


# f * * k
"""

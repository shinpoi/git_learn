# python2or3
import jinja2  # jinja2.Template() will check arg by isinstance(arg, str)

"""
$ echo 'this is a.out' > a.out
$ python lazy_load_str.py
1. init MyStr
2. init TestClass
3. do template
5. call MyStr.__str__()
4. call MyStr.load()
this is a.out
"""

class MyStr(str):
    def __new__(cls, *args, **kw):
        obj = str.__new__(cls, 'init')
        return obj

    def __init__(self, filename, ex_params=None):
        self.filename = filename
        self.ex_params = ex_params
        self.content = None

    def load(self):
        print('4. call MyStr.load()')
        with open(self.filename, 'r') as f:
            content = f.read()

        # done something by ex_params
        self.content = content
        return content

    def __str__(self):
        print('5. call MyStr.__str__()')
        if self.content:
            return self.content
        return self.load()
    __repr__ = __str__


class TestClass:
    def __init__(self, hql):
        self.hql = hql

    def do_something(self):
        t = jinja2.Template(self.hql)
        print(t.render())


if __name__ == '__main__':
    print('1. init MyStr')
    mystr = MyStr('a.out')

    print('2. init TestClass')
    tclass = TestClass(mystr)

    print('3. do template')
    tclass.do_something()


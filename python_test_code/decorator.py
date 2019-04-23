import time
import functools as ft

def log(func):
    @ft.wraps(func)
    def wrapper():
        print('call %s() by log()' % func.__name__)
        return func()
    return wrapper

@log
def now():
    print('my name is: %s()' % now.__name__)

# now = log(now)

############################
print("set n()")
n = now
print("call n()")
n()

import numpy as np
from ctypes import *

t = cdll.LoadLibrary('./t.so')
x = np.arange(1, 21, 1)

t.plus_array(x.ctypes.data_as(POINTER(c_long)), len(x))
print(x)

t.plus_array2.restype=np.ctypeslib.ndpointer(dtype=c_long, shape=(20,))
x1 = t.plus_array2(x.ctypes.data_as(POINTER(c_long)), len(x))
print(x1)

x1 = t.plus_array2(x1.ctypes.data_as(POINTER(c_long)), len(x1))
print(x1)

"""
考察：
可以直接通过指针操作更改数组。或者以生命周期在函数外（如static）的数组指针传回python
传回的数组不能为函数内变量，否则无法传回
"""

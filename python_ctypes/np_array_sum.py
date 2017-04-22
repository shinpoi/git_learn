import numpy as np
from ctypes import *

# load dll
sum_test = cdll.LoadLibrary('./np_array_sum.so')
sum_test2 = np.ctypeslib.load_library('np_array_sum.so', '.')

# create 2-dim array
x = np.arange(1, 21, 0.1).reshape((-1, 2))

# use ctypes.cdll.LoadLibrary
sum_test.mysum2.restype = c_double
s1 = sum_test.mysum2(x.ctypes.data_as(POINTER(c_double)), x.ctypes.strides, x.ctypes.shape)

# use np.ctypeslib.load_library()
sum_test2.mysum2.restype = c_double
s2 = sum_test2.mysum2(x.ctypes.data_as(POINTER(c_double)), x.ctypes.strides, x.ctypes.shape)

print(s1, s2)

"""
考察：
载入.so库时用 ctypes.cdll.LoadLibrary() 和 np.ctypeslib.load_library() 都行. 
x.ctypes.strides 和 x.ctypes.shape 会传入 long (python中的int64).
一定要在python中指定返回类型(restype = )，否则会默认解析为int16？

"""

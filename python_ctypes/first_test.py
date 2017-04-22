import ctypes
import time

def sumpy(a):
	sum = 0
	for i in range(a):
		if i%2 == 0:
			sum += a
		else:
			sum += -a
	return sum


def timer(f):
	t = time.time()
	f(99999999)
	return time.time() - t

libc = ctypes.cdll.LoadLibrary("./libpy.so")
print("C lib was Loaded, wait seconds...")

print("Python: %f" % timer(sumpy))
print("C: %f" % timer(libc.summ))


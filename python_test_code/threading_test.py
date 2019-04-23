# test: interuppt by keyboard used threading

import threading
import time

flag = 0

def counter(waittime=5):
	global flag
	while True:
		print("flag is %d..." % flag)
		time.sleep(waittime)
		if flag:
			print('get esc singal!')
			return 0

t = threading.Thread(target=counter, args=(3,))
t.start()

while True:
	s = str(input("input 'esc' to escape...\n"))
	print("your input is: %s" % s)
	if s == 'esc':
		flag = 1
		break

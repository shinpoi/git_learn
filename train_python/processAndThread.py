import multiprocessing
import subprocess
import threading
import os

def p_id(name):
    print("%s - pid: %d" % (name, os.getpid()) )

mp = multiprocessing.Process(target=p_id, args=('multi_process',))
th = threading.Process(target=p_id, args=('sub_thread',))
pid_sb = subprocess.check_output(['python3', 'pid.py'])

print("main process - pid: %d" % os.getpid())
mp.start()
th.start()
print("sub_process - pid: %s" % pid_sb)

'''
# pid.py
import os
print(os.getpid())
'''

'''
# output sample:

> main process - pid: 4487
> sub_thread - pid: 4487
> sub_process - pid: b'4488\n'
> multi_process - pid: 4489
'''

'''
# Why do new objects in multiprocessing have the same id?
https://stackoverflow.com/questions/33662292/why-do-new-objects-in-multiprocessing-have-the-same-id
'''

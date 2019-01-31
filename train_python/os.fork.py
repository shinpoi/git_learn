import os
import time

for i in range(2):
    print('**********[%d] start: %d***********' % (os.getpid(), i))
    pid = os.fork()
    print("[%d] get_pid: %d:" % (os.getpid(), pid))
    if pid == 0:
        # We are in the child process.
        print("[%d] (I'm child) just was created by %d." % (os.getpid(), os.getppid()))
    else:
        # We are in the parent process.
        print("[%d] (I'm parent) just created %d." % (os.getpid(), pid))
    print('**********[%d] end: %d***********' % (os.getpid(), i))
    
'''
e.g.

                          -- 3800 (get: 0)
                          |
  <loop: 0>               |
3798 --- 3798(get: 3799) --- 3798 (get: 3800)
      |               <loop: 1>
      |       
      -- 3799(get: 0) ------ 3799 (get: 3801)
           |
           ------ 3801 (get: 0)
'''

import os


pid=os.fork()

if pid >0:
    print("Fork above 0,PID:",os.getpid())
    print("Spawned child's PID:",pid)
else:
    print("Fork is 0, this is a child PID:",os.getpid())
    print("Parent PID:",os.getppid())
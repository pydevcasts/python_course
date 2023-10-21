import os


# def child_process():
#     print("This is the child process with the PID:%d" %os.getpid())

# def parent_process():
#     print("This is the parent with PID: %d" %os.getpid())

#     n = os.fork()
#     if n == 0:
#         child_process()
#     elif n>0:
#         print("This is the parent process with a child wich its PID is:%d" %n)
    
#     while True:
#         pass

# parent_process()

# ==================================
os.fork()
os.fork()
print("hello ...")



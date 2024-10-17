from threading import Thread
from time import sleep

def my_function_1(arg):
    for i in range(arg):
        print("Child thread-1 running and so tired now!", i)
        sleep(0.5)

def my_function_2(args):
    for i in range(args):
        print("Child thread-2 running", i)
        sleep(0.1)

#Create thread objects
t1 = Thread(target=my_function_1, args=(10,))
t2 = Thread(target=my_function_2, args=(50,))

#Start the first thread and wait it to complete
t1.start()
t1.join(timeout=4)
#  ^^^^^^^^^^^^^^^
# Thread.join(timeout=float_literal) method waits the thread
# until specified timeout value time, after which continues to run main thread
# asynchronously!


#Start the second thread and wait it to conplete
t2.start()
t2.join()

print("Main thread finished. Exiting...")
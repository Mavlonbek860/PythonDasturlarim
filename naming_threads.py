from threading import Thread
import threading
from time import sleep

def my_function_1(args):
    threading.current_thread().name = "custom name"
    print("This thread's name is: ", threading.current_thread().name)

#Create new threads
thread1 = Thread(target=my_function_1, name="My_thread", args=(2,))
thread2 = Thread(target=my_function_1, args=(3,))

print("This thread's name is: ", threading.current_thread().name)

#Start the first thread and wait it to complete
thread1.start()
thread1.join()

#Start the second thread and wait it to complete
thread2.start()
thread2.join()


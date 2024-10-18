from threading import Thread
import threading
from time import sleep

def my_function_1(args):
    print("This thread's name is: ", threading.current_thread().name)

#Create new threads
thread1 = Thread(target=my_function_1, name="My_thread", args=(2,))
thread2 = Thread(target=my_function_1, args=(3,))


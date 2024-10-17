import _thread
import time

#Define a function for a thread
def thread_task(threadName, delay):
    for count in range(1, 6):
        time.sleep(delay)
        print("Thread name: {}, count: {}.".format(threadName, count))
    print("Exiting thread {}".format(threadName,))

#Create two threads as follows:
try:
    _thread.start_new_thread(thread_task, ("Thread-1", 2,))
    _thread.start_new_thread(thread_task, ("Thread-2", 3,))
except:
    print("Error: unable to start thread")

while True:
    pass

thread_task("test", 0.5)

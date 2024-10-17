import threading

def fun(x):
    print("Current thread details: {}".format(threading.current_thread()))
    for n in range(x):
        print("{} running".format(threading.current_thread().name), n)
    print("Internal thread finished...")

#Create new thread objects
t1 = threading.Thread(target=fun, args=(100,))
t2 = threading.Thread(target=fun, args=(100,))

#Start new threads
print("Thread state: CREATED.")
t1.start()
t2.start()

#Wait for threads to complete
t1.join()
t2.join()
print("Thread state: FINISHED.")

#Simulate main thread work
for i in range(100):
    print("Main thread running", i)
print("Main thread finished...")

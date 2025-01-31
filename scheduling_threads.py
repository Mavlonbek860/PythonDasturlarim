import threading
import time

def schedule_event(name, start):
	now = time.time()
	elapsed = int(now - start)
	print("Elapsed: ", elapsed, "Name: ", name)

#Start time:
start = time.time()
print("Start time: ", time.ctime(start))

t1 = threading.Timer(3, schedule_event, args=("Event-1", start))
t2 = threading.Timer(2, schedule_event, args=("Event-2", start))

#Start the timers
t1.start()
t2.start()

t1.join()
t2.join()

#End time
end = time.time()
print("End time: ", time.ctime(end))
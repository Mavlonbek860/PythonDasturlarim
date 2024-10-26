import  threading
import time

def func(x):
	print("Current thread details: ", threading.current_thread())
	for n in range(x):
		print("Internal thread running:", n)
	print("Internal thread finished.")

t = threading.Thread(target=func, args=(6,))
t.start()

for i in range(4):
	print("Main Thread running, ", i)
print("Main thread finished.")


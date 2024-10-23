from multiprocessing.dummy import Pool as ThreadPool
import time

def square(number):
	sqr = number * number
	time.sleep(1)
	print("Number: {}, square: {}".format(number, sqr))

def cube(number):
	cub = number * number * number
	time.sleep(1)
	print("Number: {}, cube: {}".format(number, cub))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pool = ThreadPool(3)
pool.map(square, numbers)
pool.map(cube, numbers)
pool.close()
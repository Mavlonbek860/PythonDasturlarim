from threading import Thread

def add_nums(x, y):
    res = x + y
    print("addition of {} and {} equals to {}".format(x, y, res))

def cube_num(i):
    res = i ** 3
    print("Cube of {} is {}".format(i, res))

def basic_fun():
    print("Basic function is running concurrently...")

Thread(target=add_nums, args=(2, 4)).start()
Thread(target=cube_num, args=(4,)).start()
Thread(target=basic_fun).start()

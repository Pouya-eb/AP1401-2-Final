import time


def timing(func):
    def wrapper(n):
        t1 = time.time()
        func(n)
        t2 = time.time()
        print(f"Time neede is : {t2 - t1}")
        return

    return wrapper
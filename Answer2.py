import time


def timing(func):
    def wrapper(n):
        t1 = time.time()
        func(n)
        t2 = time.time()
        print(f"Time neede is : {t2 - t1}")
        return

    return wrapper


def memorize(func):
    cached = dict()

    def wrapper(n):
        if n in cached.keys():
            print("Mode : return from cache")
            print(f"Sum is : {cached[n]}")
            return cached[n]
        res = func(n)
        cached[n] = res
        print("Mode : calculated")
        print(f"Sum is : {res}")
        return res

    return wrapper
import time
from functools import wraps


def timeit(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        stop = time.time()
        print(f"Funkcja wykonywała się {stop-start}s")

        return result

    return wrapper


@timeit
def sleep_3s():
    time.sleep(1)
    time.sleep(1)
    time.sleep(1)


sleep_3s()

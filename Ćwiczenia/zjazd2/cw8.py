from functools import wraps

COUNTER = 0


def try_3_times(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                result = func(*args, **kwargs)
                return result
            except TimeoutError:
                print("Try again")

    return wrapper


@try_3_times
def ok_3rd_time():
    global COUNTER
    COUNTER += 1

    if COUNTER < 3:
        raise TimeoutError
    else:
        return 42


ok_3rd_time()

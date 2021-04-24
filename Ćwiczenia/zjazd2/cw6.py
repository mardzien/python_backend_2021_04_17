from functools import wraps


def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper doc"""
        result = f"<b>{func(*args, **kwargs)}</b>"

        return result

    return wrapper


def italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper doc"""
        result = f"<i>{func(*args, **kwargs)}</i>"

        return result

    return wrapper


@bold
@italic
def text(arg: str) -> str:
    """Mega ważna funkcja z ważną dokumentacją"""
    return f'Test {arg}'


print(text.__doc__)
print(text.__name__)
print(text.__annotations__)


def test_text_wrapper():
    assert text("cos") == '<b><i>Test cos</i></b>'

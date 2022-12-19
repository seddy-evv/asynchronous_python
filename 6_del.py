"""
Run example:
python -i 6_del.py
g = delegator(subgen())
g.send(1)
g.send(2)
try:
    g.throw(StopIteration)
except StopIteration as e:
    print("Average", e.value)
"""


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class CustomException(Exception):
    pass


def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            # print("Stop iteration")
            break
        else:
            print(".......", message)

    return "Returned from subgen()"


@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except CustomException as e:
    #         g.throw(e)

    # We can replace the code above with:

    result = yield from g
    print(result)

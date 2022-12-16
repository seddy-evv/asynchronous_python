"""
Run example:
python -i 5_coroutines.py
g = average()
g.send(5)
g.send(1)
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


def subgen():
    x = "Ready to accept message"
    message = yield x
    print("Subgen received:", message)


class CustomException(Exception):
    pass


@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print("Done")
            break
        except CustomException:
            print("..............")
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)

    return average

from time import sleep

queue = []


def counter():
    count = 0
    while True:
        print(count)
        count += 1
        yield


def printer():
    count = 0
    while True:
        if count % 3 == 0:
            print("Bang!")
        count += 1
        yield


def main():
    while True:
        g = queue.pop(0)
        next(g)
        queue.append(g)
        sleep(0.5)


if __name__ == "__main__":
    g1 = counter()
    queue.append(g1)
    g2 = printer()
    queue.append(g2)
    main()

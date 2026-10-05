from itertools import islice, takewhile


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print(list(islice(fibonacci(), 10)))
print(list(takewhile(lambda n: n < 100, fibonacci())))

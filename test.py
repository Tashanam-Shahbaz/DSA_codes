def fib(n):
    assert n > - 1
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


fib(5)


def goodfib(n):
    assert n > -1
    if n == 0: return 1, 0
    (a, b) = goodfib(n - 1)
    print(a)
    return a + b, a

# print(goodfib(5))

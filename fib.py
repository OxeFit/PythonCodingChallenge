def fib_number(n: int) -> int:
    if (n == 0):
        return 0

    if (n == 1):
        return 1

    return fib_number(n-1) + fib_number(n-2)

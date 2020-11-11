def fib_number(n: int) -> int:
    if (n == 0):
        return 0

    if (n == 1):
        return 1
    
    fib_n = 0
    fib_n1_prev = 1
    fib_n2_prev = 0
    for i in range(0,n-1):
        fib_n = fib_n1_prev + fib_n2_prev
        fib_n2_prev = fib_n1_prev
        fib_n1_prev = fib_n
    
    return fib_n

print(fib_number(6))
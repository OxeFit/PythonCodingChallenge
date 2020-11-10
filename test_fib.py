from fib import *


def test_compute_fib_number():
    assert fib_number(1) == 1
    assert fib_number(2) == 1
    assert fib_number(3) == 2
    assert fib_number(4) == 3
    assert fib_number(5) == 5
    assert fib_number(6) == 8

    assert fib_number(13) == 233
    assert fib_number(1000) == 987

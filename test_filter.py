from filter import *
import random


def test_filter_from_break_freq():
    filter = AlphaFilter.from_break_freq(0.0, 0.001)
    assert filter.alpha == 1.0

    filter = AlphaFilter.from_break_freq(math.inf, 0.001)
    assert filter.alpha == 0.0


def test_filter_simple():
    filter = AlphaFilter(0.8, 0.001)
    assert filter.alpha == 0.8
    assert filter.sample_dt == 0.001

    initial_position = 10
    simulated_noise = 0

    filter.do_filter(initial_position)

    """The filter should set itself to exactly the input the first time it is called"""
    assert filter.value() == initial_position

    for i in range(10000):
        if i % 2 == 0:
            simulated_noise = random.random()

        current_value = filter.value()
        new_value = current_value + (math.pow(-1, i) * simulated_noise)
        filter.do_filter(new_value)

    assert math.abs(filter.value() - initial_position) < 0.0001


def test_reset_filter():
    filter = AlphaFilter(0.8, 0.001)
    assert filter.alpha == 0.8
    assert filter.sample_dt == 0.001

    initial_position = 10
    simulated_noise = 0

    filter.do_filter(initial_position)

    for i in range(10000):
        filter.do_filter(random.random())

    filter.reset()
    filter.do_filter(initial_position)

    """The filter should set itself to exactly the input the first time it is called"""
    """As such, this should hold after the reset method is called"""
    assert filter.value() == initial_position

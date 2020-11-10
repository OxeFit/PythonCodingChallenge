from filter import *


def test_filter_from_break_freq():
    filter = AlphaFilter.from_break_freq(0.0, 0.001)
    assert filter.alpha == 1.0

    filter = AlphaFilter.from_break_freq(math.inf, 0.001)
    assert filter.alpha == 0.0

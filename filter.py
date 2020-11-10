import math


def clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)


def break_frequency_from_alpha(alpha: float, dt: float) -> float:
    return (1.0 - alpha) / (math.pi * dt + math.pi * alpha * dt)


def alpha_from_break_frequency(freq: float, dt: float) -> float:
    if not math.isinf(freq):
        omega = 2.0 * math.pi * freq
        alpha = (1.0 - omega * dt / 2.0) / (1.0 + omega * dt / 2.0)
        return clamp(alpha, 0.0, 1.0)
    else:
        return 0.0


class AlphaFilter:
    """An Alpha Filter is a single pole low pass filter; put another way, it's an alpha-beta filter w/ beta = 0"""

    def __init__(self, alpha: float, sample_dt: float) -> None:
        self.alpha = alpha
        self.sample_dt = sample_dt

    def __repr__(self):
        return "AlphaFilter[alpha: %s dt:%s]" % (self.alpha, self.sample_dt)

    @classmethod
    def from_break_freq(cls, freq: float, sample_dt: float):
        alpha = alpha_from_break_frequency(freq, sample_dt)
        return cls(alpha, sample_dt)

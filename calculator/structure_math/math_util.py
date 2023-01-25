from math import sin, cos, tan, pi


class MappingError(ValueError):
    pass


def in_range(number: float,  target: float, delta: float = 1E-10) -> bool:
    return target - delta < number and number < target + delta


def round_with_range(number: float, target: float, delta: float = 1E-10) -> float:
    if in_range(number, target, delta):
        return target
    else:
        return number


def round_sin(radian: float) -> float:

    remain: float = radian % (pi * 2)
    if (in_range(radian % pi, 0)):
        return 0.0
    elif in_range(remain, pi / 2) or in_range(remain, -pi * 3 / 2):
        return 1.0
    elif in_range(remain, -pi / 2) or in_range(remain, pi * 3 / 2):
        return -1.0
    else:
        return sin(radian)


def round_cos(radian: float) -> float:
    remain: float = radian % (pi * 2)
    if (in_range(radian % (pi * 2), 0) or in_range(radian % (pi * 2), 2 * pi) or in_range(radian % (pi * 2), -2 * pi)):
        return 1.0
    elif (in_range(radian % pi, 0)):
        return -1.0
    elif (in_range(remain, pi / 2) or in_range(remain, -pi * 3 / 2)):
        return 0.0
    else:
        return cos(radian)


def round_tan(radian: float) -> float:
    remain: float = radian % (pi * 2)
    if in_range(remain % pi, 0):
        return 0.0
    elif in_range(remain, pi / 2) or in_range(remain, -pi * 3 / 2):
        return float('inf')
    elif in_range(remain, -pi / 2) or in_range(remain, pi * 3 / 2):
        return -float('inf')
    else:
        return tan(radian)

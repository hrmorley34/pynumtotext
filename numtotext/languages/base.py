from collections.abc import Mapping


class NumbersBase:
    ZERO: str
    # value for 0 alone or before decimal point

    NEGATIVE: str
    # name for 'minus'

    ONE_THRESHOLD: int
    # add one to all parts above this eg. 100 -> [one] hundred

    NUMBERS: Mapping[int, str]
    # 0 -> digit zero
    # 1 -> digit one
    # 13 -> preventing ten-one
    # 20 -> twenty
    # no 21 -> implied by 20 and 1
    # 100, 1000, 1 000 000, 1 000 000 000, etc.

    JOINS: Mapping[int, str]
    # 0 -> (decimal seperator)
    # 1 -> between 10**1 and 10**0 (ie. "thirty[-]two")
    # 2 -> one hundred [and] twenty-three

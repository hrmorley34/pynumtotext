from .base import NumbersBase


class Numbers_EN(NumbersBase):
    ZERO = "zero"
    # ZERO = "nought"

    NEGATIVE = "minus"
    # NEGATIVE = "negative"

    ONE_THRESHOLD = 10**2  # add one to all parts above this eg. [one] hundred
    COUNT_JOIN = " "  # three[ ]hundred

    NUMBERS = {
        0: "oh",
        # 0: "nought",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        10**2: "hundred",
        10**3: "thousand",
        10**6: "million",
        10**9: "billion",
        10**12: "trillion",
        10**15: "quadrillion",
        10**18: "quintillion",
        10**21: "sextillion",
        10**24: "septillion",
    }

    JOINS = {
        0: " point ",  # (decimal seperator)
        1: "-",  # between 10**1 and 10**0 (ie. "thirty[-]two")
        2: " and ",  # one hundred [and] twenty-three
        # 2: " ",  # one hundred twenty-three
    }


class Numbers_US(Numbers_EN):
    JOINS = {
        0: " point ",  # (decimal seperator)
        1: "-",  # between 10**1 and 10**0 (ie. "thirty[-]two")
        # 2: " and ",  # one hundred [and] twenty-three
        2: " ",  # one hundred twenty-three
    }


class Numbers_EN_Long(Numbers_EN):
    NUMBERS = {
        0: "oh",
        # 0: "nought",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        10**2: "hundred",
        10**3: "thousand",
        10**6: "million",
        10**9: "milliard",
        10**12: "billion",
        10**15: "billiard",
        10**18: "trillion",
        10**21: "trilliard",
        10**24: "quadrillion",
        10**27: "quadrilliard",
        10**30: "quintillion",
        10**33: "quintilliard",
        10**36: "sextillion",
        10**39: "sextilliard",
        10**42: "septillion",
        10**45: "septilliard",
    }


class Numbers_EN_Longer(Numbers_EN):
    NUMBERS = {
        0: "oh",
        # 0: "nought",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        10**2: "hundred",
        10**3: "thousand",
        10**6: "million",
        # 10**9: "milliard",
        10**12: "billion",
        10**24: "trillion",
        10**48: "quadrillion",
        10**96: "quintillion",
        10**192: "sextillion",
        10**384: "septillion",
    }

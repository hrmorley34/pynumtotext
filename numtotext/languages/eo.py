from .base import NumbersBase


class Numbers_EO(NumbersBase):
    ZERO = "nul"

    NEGATIVE = "minus"

    ONE_THRESHOLD = 10**6  # add one to all parts above this eg. [unu] miliono
    COUNT_JOIN = ""  # tri[]cent; TODO: fix du{ }mil

    NUMBERS = {
        0: "nul",
        1: "unu",
        2: "du",
        3: "tri",
        4: "kvar",
        5: "kvin",
        6: "ses",
        7: "sep",
        8: "ok",
        9: "naŭ",
        10**1: "dek",
        10**2: "cent",
        10**3: "mil",
        10**6: "miliono",  # TODO: append 'j' for plurals
        10**9: "miliardo",
        10**12: "biliono",
    }

    JOINS = {
        0: " point ",  # (decimal seperator)
        # all others default to spaces
    }

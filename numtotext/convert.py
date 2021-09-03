from math import log10
from typing import Type
from .languages.base import NumbersBase
from .languages.en import Numbers_EN


def int_to_words(n: int, numbers: Type[NumbersBase] = Numbers_EN) -> str:
    n = int(n)
    if n == 0:
        # ZERO is special case
        return numbers.ZERO
    elif n < 0:
        # prefix with 'minus', and treat the rest of the number as positive
        text = [numbers.NEGATIVE, " "]
        n = abs(n)
    else:
        # no 'minus' prefix
        text = []

    # check for presence of largest part, then smaller
    # (check for thousands, then hundreds, ..., 19 before 10, down to 1)
    for size, word in sorted(numbers.NUMBERS.items(), reverse=True):
        if n <= 0:
            # No remaining number (taken by a previous iteration)
            break

        # split into part (* size), n (remainder)
        # e.g. n=12345, size=1000 -> part=12, n=345
        part = n // size
        n %= size

        if part < 1:
            # No number in this part (go check a smaller part)
            continue
        elif part != 1 or size >= numbers.ONE_THRESHOLD:
            # Add a prefix ([three] hundred; [one] thousand)
            # Recalculate sub-part (e.g. 123000 -> [one hundred and twenty-three] thousand)
            text.append(int_to_words(part, numbers=numbers))
            text.append(numbers.COUNT_JOIN)
        text.append(word)

        # Fetch join to next part
        text.append(numbers.JOINS.get(int(log10(size)), " "))

    # ignore last join e.g. "one hundred [and]" or "sixty[-]" when nothing after
    return "".join(text[:-1]).strip()


def float_to_words(n: float, precision: int = 10, numbers: Type[NumbersBase] = Numbers_EN) -> str:
    n = float(n)
    if n == 0:
        # ZERO is special case
        return numbers.ZERO
    elif n < 0:
        # prefix with 'minus', and treat the rest of the number as positive
        text = numbers.NEGATIVE + " "
        n = abs(n)
    else:
        text = ""

    # for part before decimal point, convert as integer
    text += int_to_words(int(n), numbers=numbers)

    # 123.456 -> 4.56
    n = (n % 1) * 10
    if n == 0:
        # no decimal part; return the generated integer part
        return text.strip()

    # add the decimal point name
    text += numbers.JOINS.get(0, " point ")

    # add the names of each digit in turn
    while n:
        text += numbers.NUMBERS[int(n)] + " "

        if precision is not None:
            n = round(n % 1, precision) * 10
        else:
            n = (n % 1) * 10

    return text.strip()

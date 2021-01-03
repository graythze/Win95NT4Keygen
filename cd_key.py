# XXX-XXXXXXX
import random


def cd_keygen_first_segment():
    first_seg_not_allowed = [333, 444, 555, 666, 777, 888]
    first_seg = str(random.randint(0, 998))
    while first_seg in first_seg_not_allowed:
        first_seg = str(random.randint(0, 998))

    return str(first_seg).rjust(3, '0')


def cd_keygen_seven_digit():
    six_digits = str(random.randint(0, 999999))
    seventh_digit = random.randint(0, 9)
    while seventh_digit == 0 or seventh_digit >= 8:
        seventh_digit = random.randint(0, 9)
    seven_digits = (six_digits + str(seventh_digit)).rjust(7, '0')

    sum = 0
    for x in seven_digits:
        sum += int(x)

    return seven_digits, sum


def check_seven_digit():
    seven_digits, sum = cd_keygen_seven_digit()
    while sum % 7 != 0:
        seven_digits, sum = cd_keygen_seven_digit()

    return seven_digits

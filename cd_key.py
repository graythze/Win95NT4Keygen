# XXX-XXXXXXX
import random


def cd_keygen_first_segment():
    first_seg_not_allowed = [333, 444, 555, 666, 777, 888]
    first_seg = random.randint(0, 998)
    while first_seg in first_seg_not_allowed:
        first_seg = random.randint(0, 998)

    return str(first_seg).zfill(3)


def cd_keygen_seven_digit():
    six_digits = str(random.randint(0, 999999))
    seventh_digit = random.randint(1, 7)
    # while seventh_digit == 0 or seventh_digit >= 8:
    #     seventh_digit = random.randint(0, 9)
    seven_digits = (six_digits + str(seventh_digit)).zfill(7)

    sum = 0
    for x in seven_digits:
        sum += int(x)

    return seven_digits, sum


def check_seven_digit():
    seven_digits, sum = cd_keygen_seven_digit()
    while sum % 7 != 0:
        seven_digits, sum = cd_keygen_seven_digit()

    return seven_digits


def check_cd_key(key):
    key_split = key.split("-")

    first_seg_not_allowed = [333, 444, 555, 666, 777, 888]

    if int(str(key_split[0])) in range(0, 998 + 1) and int(str(key_split[0])) not in first_seg_not_allowed:
        print("first seg is ok")
        first_seg = True
    else:
        first_seg = False

    sum = 0
    for digit in key_split[1]:
        sum += int(digit)

    if sum % 7 == 0:
        print("sum is ok")
        sum_of_digits = True
    else:
        sum_of_digits = False

    if int(key_split[1][6]) in range(1, 7 + 1):
        print("last digit is ok")
        check_digit = True
    else:
        check_digit = False

    if (first_seg & sum_of_digits & check_digit) is True:
        print("key is valid")
    else:
        print("key is invalid")
# XXXXX-OEM-XXXXXXX-XXXXX
import random
from generator import pass_check as passch
from generator import fail_check as failch

def oem_first_segment():
    years = ["95", "96", "97", "98", "99", "00", "01", "02", "03"]
    three_digits = str(random.randint(1, 366))

    if len(three_digits) in range(1, 2 + 1):
        three_digits = three_digits.zfill(3)

    two_digits = str(random.choice(years))
    return three_digits + two_digits

def oem_second_segment():
    middle_digits = str(random.randint(0, 99999)).zfill(5)
    last_digit = random.randint(1, 7)

    second_segment = (middle_digits.zfill(5) + str(last_digit)).zfill(7)

    sum = 0
    for x in second_segment:
        sum += int(x)

    return second_segment, sum


def check_second_digit():
    seven_digits, sum = oem_second_segment()

    while sum % 7 != 0:
        seven_digits, sum = oem_second_segment()
    return seven_digits


def oem_third_segment():
    third_segment = str(random.randint(0, 99999))
    return third_segment.zfill(5)


def check_oem_key(key):
    key_split = key.split("-")

    years = ["95", "96", "97", "98", "99", "00", "01", "02", "03"]

    if str(key_split[0][3] + key_split[0][4]) in years:
        print(f"{passch}: The year is OK")
        year = True
    else:
        year = False

    if int(key_split[0][0] + key_split[0][1] + key_split[0][2]) in range(1, 366 + 1):
        print(f"{passch}: 3 digs ok")
        three_digits = True
    else:
        three_digits = False

    if int(key_split[2][0]) == 0:
        print(f"{passch}: first zero is ok")
        zero_digit_first = True
    else:
        zero_digit_first = False

    sum = 0
    for digit in key_split[2][1:]:
        sum += int(digit)

    if sum % 7 == 0:
        print(f"{passch}: sum is ok")
        sum_of_digits = True
    else:
        sum_of_digits = False

    if len(key_split[3]) == 5 and key_split[3].isnumeric():
        print(f"{passch}: last part is ok")
        last_digit_part = True
    else:
        last_digit_part = False

    if (year & three_digits & zero_digit_first & sum_of_digits & last_digit_part) is True:
        print(f"{passch}: Provided key is valid")
    else:
        print(f"{failch}: Provided key is invalid")
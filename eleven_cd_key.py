# XXXX-XXXXXXX
import random


def eleven_cd_keygen_first_segment():
    first_segment = str(random.randint(1, 9991)).zfill(4)
    last_digit = int(first_segment[2]) + random.randint(1, 2)

    if last_digit == 10:
        first_segment = str(first_segment[0] + first_segment[1] + first_segment[2] + "0")
    elif last_digit == 11:
        first_segment = str(first_segment[0] + first_segment[1] + first_segment[2] + "1")
    else:
        first_segment = str(first_segment[0] + first_segment[1] + first_segment[2] + str(last_digit))

    return first_segment


def keygen_seven_digit():
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
    seven_digits, sum = keygen_seven_digit()
    while sum % 7 != 0:
        seven_digits, sum = keygen_seven_digit()

    return seven_digits


def check_eleven_cd_key(key):
    key_split = key.split("-")

    if int(str(key_split[0])) in range(1, 9991 + 1):
        digit_range = True
    else:
        digit_range = False

    fourth_digit = int(key_split[0][2]) + 1

    if fourth_digit == 10:
        if int(key_split[0][3]) == 0:
            fourth_digit_pass = True
        else:
            fourth_digit_pass = False
    elif fourth_digit == 11:
        if int(key_split[0][3]) == 1:
            fourth_digit_pass = True
        else:
            fourth_digit_pass = False
    elif fourth_digit == int(key_split[0][3]):
        fourth_digit_pass = True
    else:
        fourth_digit_pass = False
        print("Fourth digit check fail")

    sum = 0
    for digit in key_split[1]:
        sum += int(digit)

    if sum % 7 == 0:
        print("sum is ok")
        sum_of_digits = True
    else:
        sum_of_digits = False

    if (digit_range & fourth_digit_pass & sum_of_digits) is True:
        print("key is valid")
    else:
        print("key is invalid")


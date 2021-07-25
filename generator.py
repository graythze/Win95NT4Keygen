import argparse
import time
import cd_key
import oem_key
import eleven_cd_key


def error_msg():
    return "Looks like you've started script without arguments \n" \
           "Use 'python generator.py -c' to generate CD key \n" \
           "Use 'python generator.py -o' to generate OEM key \n" \
           "Use 'python generator.py -e' to generate 11-digit CD key \n" \
           "Use 'python generator.py -c -o -e' to generate CD, OEM and 11-digit CD key together \n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Use python generator.py <arg(s)> to generate CD, OEM or 11-digit key')
    parser.add_argument('-c', '--cdkey',
                        action='store_true',
                        help='Generate CD key')
    parser.add_argument('-o', '--oemkey',
                        action='store_true',
                        help='Generate OEM key')
    parser.add_argument('-e', '--elevencdkey',
                        action='store_true',
                        help='Generate 11-digit CD key')
    args = parser.parse_args()

    if args.cdkey is True or args.oemkey is True or args.elevencdkey is True:
        now = int(time.time())
        key_file = open("keys" + str(now) + ".txt", "w")
        if args.cdkey is True:
            cd_key = cd_key.cd_keygen_first_segment() + '-' + cd_key.check_seven_digit()
            key_file.write("CD Key: " + cd_key + "\n")
            print("CD Key has been generated")
        if args.oemkey is True:
            oem_key = oem_key.oem_first_segment() + '-OEM-' + oem_key.check_second_digit() + '-' + oem_key.oem_third_segment()
            key_file.write("OEM Key: " + oem_key + "\n")
            print("OEM Key has been generated")
        if args.elevencdkey is True:
            cd_key_2 = eleven_cd_key.eleven_cd_keygen_first_segment() + '-' + eleven_cd_key.check_seven_digit()
            key_file.write("11-digit CD Key: " + cd_key_2 + "\n")
            print("11-digit CD Key has been generated")
    else:
        print(error_msg())
        input("Press ENTER to exit")


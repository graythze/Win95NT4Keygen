import argparse
import time
import cd_key
import oem_key
import eleven_cd_key

pass_check = "[OK]"
fail_check = "[FAIL]"

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
    parser.add_argument('-s', '--savetofile',
                        action='store_true',
                        help='Save key(s) to file')
    parser.add_argument('-ch', '--check',
                        type=str,
                        help='Check if key is valid')
    args = parser.parse_args()

    if args.cdkey is True or args.oemkey is True or args.elevencdkey is True or args.check:
        now = int(time.time())
        if args.cdkey is True:
            cd_key = cd_key.cd_keygen_first_segment() + '-' + cd_key.check_seven_digit()

            print(f"CD Key has been generated: {cd_key}\n")

            if args.savetofile is True:
                key_file = open("CD_Key_" + str(now) + ".txt", "w")
                key_file.write("CD Key: " + cd_key + "\n")

                print(f"CD Key has been saved to file {"CD_Key_" + str(now) + ".txt"}")
        if args.oemkey is True:
            oem_key = oem_key.oem_first_segment() + '-OEM-' + oem_key.check_second_digit() + '-' + oem_key.oem_third_segment()

            print(f"OEM Key has been generated: {oem_key}\n")
            if args.savetofile is True:
                key_file = open("OEM_Key_" + str(now) + ".txt", "w")
                key_file.write("OEM Key: " + oem_key + "\n")

                print(f"OEM Key has been saved to file {"OEM_Key_" + str(now) + ".txt"}")
        if args.elevencdkey is True:
            cd_key_2 = eleven_cd_key.eleven_cd_keygen_first_segment() + '-' + eleven_cd_key.check_seven_digit()

            print(f"11-digit CD Key has been generated: {cd_key_2}\n")
            if args.savetofile is True:
                key_file = open("CD_11_Key_" + str(now) + ".txt", "w")
                key_file.write("11 OEM Key: " + cd_key_2 + "\n")

                print(f"11-digit CD Key has been saved to file {"CD_11_Key_" + str(now) + ".txt"}")
        if args.check:
            splitted = args.check.split("-")
            print(splitted)
            if len(str(splitted[0])) == 3:
                print("Looks like you've provided CD key")
                cd_key.check_cd_key(args.check)
            elif len(str(splitted[0])) == 4:
                print("Looks like you've provided 11-digit CD key")
                eleven_cd_key.check_eleven_cd_key(args.check)
            elif len(str(splitted[0])) == 5:
                print("Looks like you've provided OEM key")
                oem_key.check_oem_key(args.check)
            else:
                print("You've provided invalid key.")
    else:
        print(error_msg())
        input("Press ENTER to exit")

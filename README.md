# MS Office 97 and Windows 95 Key Generator

### CD Key
*Makes a CD Key which looks like XXX-XXXXXXX.*

The first segment is the site number. It can be **from 000 to 998**. Some numbers like **333, 444, 555, 666, 777, 888, 999** aren't allowed

The sum of second segment must be divisible by seven, and the last digit cannot be **0 or >= 8**

*****The most basic valid key is 000-0000007*****

### OEM Key
*Makes a OEM Key which looks like XXXXX-OEM-XXXXXXX-XXXXX.*

The first segment is the random three digits and date. The first three digits **can be anything from 001 to 366**, and the last two are the year, **anything from 95 to 03**

The second segment has first 0 digit at start. The next digits can be generated to identical CD keys.

The third segment has fully random digits.

*****The most basic valid key is 00100-OEM-0000007-00000*****

### 11-digit CD Key
*Makes a 11-digit CD Key which looks like XXXX-XXXXXXX.*

The first segment is the site number. It can be from **0001 to 9991**. The last digit much be **3rd digit + 1 or 2**. When the result is **> 9**, it overflows to **0 or 1**.

The sum of second segment must be divisible by seven, and the last digit cannot be **0 or >= 8** (identical CD Keys)

*****The most basic valid key is 0001-0000007*****

# Usage
* Use `python generator.py -c` to *generate CD key*
  
  Use `python generator.py -o` to *generate OEM key*

  Use `python generator.py -e` to *generate 11-digit CD key*

  Use `python generator.py -c -o -e` to *generate CD, OEM and 11-digit CD key together*

* File `keys<unixDate>.txt` will be created. Open it to get keys

# Sources
***Windows NT 4.0 and Windows 95 Key Generator*** by ***[@nilaerdna](https://github.com/nilaerdna/Windows95NT4KeyGenerator)***

***Examining the Microsoft mod7 product key algorithm*** by ***[@dgurney](https://gurney.dev/posts/mod7/)***

**Leaked Windows NT 4 source code***

**this code was made **only** for educational purposes. Use it at your own risk*
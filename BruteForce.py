import hashlib
import binascii
import random
import string
import socket


class MyString(str):
    def __add__(self, x):
        # If we're trying to add anything but an int, do normal string
        # addition.
        if type(x) is not int:
            return str.__add__(self, x)

        res = ''
        i = len(self)-1
        while x > 0:
            # Get the ASCII code of the i-th letter and "normalize" it
            # so that a is 0, b is 1, etc.
            # If we are at the end of the string, make it -1, so that if we
            # need to "add" 1, we get a.
            if i >= 0:
                c = ord(self[i]) - 97
            else:
                c = -1

            # Calculate the number of positions by which the letter is to be
            # "rotated".
            pos = x % 26

            # Calculate x for the next letter, add a "carry" if needed.
            x //= 26
            if c + pos >= 26:
                x += 1

            # Do the "rotation".
            c = (c + pos) % 26

            # Add the letter at the beginning of the string.
            res = chr(c + 97) + res

            i -= 1

        # If we didn't reach the end of the string, add the rest of the string back.
        if i >= 0:
            res = self[:i+1] + res

        return MyString(res)

liste_de_char = string.ascii_letters+string.digits
tmp = 1
countnb = 0
mot = []
while tmp and countnb < 4:
    #mot.append('')
    countnb += 1
    for i in range(countnb):
        mot.append('')
        for j in range(62):
            #mot.append('')
            print(countnb)
            mot[countnb-1] = liste_de_char[j]
            # test
            print(mot)
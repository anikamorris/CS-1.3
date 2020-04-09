#!python

import math
import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    res = 0
    # Decode digits from binary (base 2)
    # Loop through each digit, add to a result based on it being multiplied 
    # by 2^len(digits) which should go down by 1 each iteration
    if base == 2:
        power = len(digits)
        for i in range(len(digits)):
            res += int(digits[i]) * int(math.pow(2, power - 1))
            power -= 1

    # Decode digits from hexadecimal (base 16)
    if base == 16:
        hex = {"a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
        power = len(digits)
        for i in range(len(digits)):
            digit = digits[i]
            if digit in string.ascii_letters:
                digit = digit.lower()
                digit = hex[digit]
            res += int(digit) * int(math.pow(16, power - 1))
            power -= 1
    # Decode digits from any base (2 up to 36)
    # ...
    else:
        strings = string.digits + string.ascii_lowercase
        digits = digits[::-1]
        for i, num in enumerate(digits):
            res += base**i * strings.index(num)
    return res

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    res = ''
    # TODO: Encode number in binary (base 2)
    # ...
    
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    for i in range(8):
        res += string.hexdigits[number % 16]
        number = number // 16

    # TODO: Encode number in any base (2 up to 36)
    # ...
    return res

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        digits = args[0]
        base = int(args[1])
        result = decode(digits, base)
        print('{} in base {} is {} in base 10.'.format(digits, base, result))
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()

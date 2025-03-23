#completely manual operations

import math

def float_to_ieee754_manual(number, bits=32):
    if bits not in (32, 64):
        return "Invalid bit size. Please choose 32 or 64."

    sign = '0' if number >= 0 else '1'
    number = abs(number)

    if number == 0.0:
        if bits == 32:
            return f"Sign: {sign}\nExponent: {'0' * 8}\nMantissa: {'0' * 23}", f"{sign}{'0' * 8}{'0' * 23}"
        else:
            return f"Sign: {sign}\nExponent: {'0' * 11}\nMantissa: {'0' * 52}", f"{sign}{'0' * 11}{'0' * 52}"

    exponent_bits = 8 if bits == 32 else 11
    mantissa_bits = 23 if bits == 32 else 52
    bias = (2**(exponent_bits - 1)) - 1

    exponent = 0
    if number >= 2.0:
        while number >= 2.0:
            number /= 2.0
            exponent += 1
    elif number < 1.0:
        while number < 1.0:
            number *= 2.0
            exponent -= 1
    exponent += bias

    exponent_binary = bin(exponent)[2:].zfill(exponent_bits)

    number -= 1.0
    mantissa_binary = ''
    for _ in range(mantissa_bits):
        number *= 2.0
        if number >= 1.0:
            mantissa_binary += '1'
            number -= 1.0
        else:
            mantissa_binary += '0'

    return f"Sign: {sign}\nExponent: {exponent_binary}\nMantissa: {mantissa_binary}", f"{sign}{exponent_binary}{mantissa_binary}"

#Example usage
number = float(input("Enter a number: "))
bits = int(input("Enter 1 for 32-bit or 2 for 64-bit: "))

if bits == 1:
    result, final_binary = float_to_ieee754_manual(number, 32)
    print("\n32-bit IEEE 754 Representation:")
    print(result)
    print(f"Hence the number: {final_binary}")

elif bits == 2:
    result, final_binary = float_to_ieee754_manual(number, 64)
    print("\n64-bit IEEE 754 Representation:")
    print(result)
    print(f"Hence the number: {final_binary}")
else:
    print("Invalid option. Please input 1 or 2.")
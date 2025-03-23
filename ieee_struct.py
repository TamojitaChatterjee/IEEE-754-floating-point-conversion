#using struct

import struct

def float_to_ieee754(number, bits=32):
    if bits not in (32, 64):
        return "Invalid bit size. Please choose 32 or 64.", None

    try:
        if bits == 32:
            packed = struct.pack('>f', number)
            binary = ''.join(f'{byte:08b}' for byte in packed)
            sign = binary[0]
            exponent = binary[1:9]
            mantissa = binary[9:]
            return f"Sign: {sign}\nExponent: {exponent}\nMantissa: {mantissa}", binary

        elif bits == 64:
            packed = struct.pack('>d', number)
            binary = ''.join(f'{byte:08b}' for byte in packed)
            sign = binary[0]
            exponent = binary[1:12]
            mantissa = binary[12:]
            return f"Sign: {sign}\nExponent: {exponent}\nMantissa: {mantissa}", binary

    except struct.error:
        return "Invalid input. Please enter a valid number.", None
    except OverflowError:
        return "Number too large for conversion.", None


if __name__ == "__main__":
    try:
        number = float(input("Enter a number: "))
        bits = int(input("Enter 1 for 32-bit representation or 2 for 64-bit representation: "))

        if bits == 1:
            result, final_binary = float_to_ieee754(number, 32)
            if final_binary is not None:
                print("\n32-bit IEEE 754 Representation:")
                print(result)
                print(f"Hence the number: {final_binary}")
            else:
                print(result)

        elif bits == 2:
            result, final_binary = float_to_ieee754(number, 64)
            if final_binary is not None:
                print("\n64-bit IEEE 754 Representation:")
                print(result)
                print(f"Hence the number: {final_binary}")
            else:
                print(result)
        else:
            print("Invalid option. Please input 1 or 2.")

    except ValueError:
        print("Invalid input. Please enter a valid number and bit option.")
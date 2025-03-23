# IEEE 754 Floating Point Converter

## Overview
This project provides two implementations of IEEE 754 floating-point conversion in Python. It allows users to convert a given floating-point number into its IEEE 754 binary representation (both 32-bit and 64-bit).

- **`ieee_math.py`**: Implements the conversion manually without using built-in libraries.
- **`ieee_struct.py`**: Utilizes Python's `struct` module for conversion.

## Features
- Supports both **single-precision (32-bit)** and **double-precision (64-bit)** conversions.
- Provides a breakdown of the **sign bit**, **exponent**, and **mantissa**.
- Offers both a **manual implementation** and a **struct-based implementation**.
- Handles edge cases such as **zero** and **very large numbers**.

## Files Included

### `ieee_math.py`
- Performs **manual IEEE 754 conversion** without using built-in modules.
- Steps:
  1. Determine the **sign bit**.
  2. Normalize the number to extract the **mantissa** and **exponent**.
  3. Convert the exponent and mantissa to **binary format**.
  4. Print and return the IEEE 754 representation.
- **Example Usage:**
  ```sh
  python ieee_math.py
  ```

### `ieee_struct.py`
- Uses Python's `struct` module for a **more efficient** IEEE 754 conversion.
- Steps:
  1. Pack the floating-point number using `struct.pack`.
  2. Extract the **binary representation**.
  3. Parse the **sign bit**, **exponent**, and **mantissa**.
- **Example Usage:**
  ```sh
  python ieee_struct.py
  ```

## Installation & Setup
### Prerequisites
- Python 3.x

### Running the Code
1. Open a terminal or command prompt.
2. Run the script:
   ```sh
   python ieee_math.py
   ```
   or
   ```sh
   python ieee_struct.py
   ```
3. Enter a floating-point number and select **1 for 32-bit** or **2 for 64-bit** representation.

## Expected Output
For `ieee_math.py` and `ieee_struct.py`, if the input number is `5.75` in 32-bit mode, the output would be:
```
Sign: 0
Exponent: 10000001
Mantissa: 01110000000000000000000
Hence the number: 01000000101110000000000000000000
```

## Project Structure
```
├── ieee_math.py         # Manual IEEE 754 conversion
├── ieee_struct.py       # IEEE 754 conversion using struct
├── README.md            # Project documentation
```

## Conclusion
This project provides a simple yet effective way to convert floating-point numbers into IEEE 754 format. The manual approach helps in understanding the underlying conversion logic, while the `struct` approach offers an optimized method.

Future improvements may include:
- Supporting more IEEE 754 formats (e.g., 16-bit half-precision).
- Implementing a function to **convert back** from IEEE 754 binary to floating-point numbers.
- Creating a **graphical interface** for user-friendly interaction.

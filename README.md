# IEEE 754 Floating-Point Representation

## Overview
This project provides implementations to convert floating-point numbers into IEEE 754 representation using both manual computation and built-in libraries in Python and C. The project includes different approaches to achieve the conversion for both 32-bit and 64-bit IEEE 754 formats.

## Features
- **Manual Conversion in Python** (`ieee_math.py`):
  - Implements IEEE 754 conversion without using built-in functions.
  - Supports both 32-bit and 64-bit representations.
- **Struct-Based Conversion in Python** (`ieee_struct.py`):
  - Uses the `struct` module for efficient IEEE 754 conversion.
  - Supports both 32-bit and 64-bit representations.
- **C-Based Conversion** (`ieee_754.c`):
  - Uses bitwise operations and type punning to extract IEEE 754 representations.
  - Provides a command-line interface for user input.

## Files Included
1. `ieee_math.py` - Manual IEEE 754 conversion using pure Python logic.
2. `ieee_struct.py` - IEEE 754 conversion using Python's `struct` module.
3. `ieee_754.c` - IEEE 754 conversion implemented in C using bitwise operations.

## Installation & Usage
### Python Implementation
Ensure you have Python installed on your system (Python 3.x recommended). 

To run the manual IEEE 754 conversion:
```sh
python ieee_math.py
```
To run the struct-based IEEE 754 conversion:
```sh
python ieee_struct.py
```

### C Implementation
Ensure you have a C compiler (such as GCC) installed.

Compile and run the program:
```sh
gcc ieee_754.c
./a.exe
```

## How It Works
### Python (Manual Computation)
- The `ieee_math.py` file calculates the IEEE 754 representation step-by-step:
  - Determines the sign bit.
  - Normalizes the number and calculates the exponent.
  - Extracts the mantissa bits manually.

### Python (Struct-Based Computation)
- The `ieee_struct.py` file utilizes Python's `struct.pack()` function to obtain IEEE 754 representation directly from memory.

### C Implementation
- The `ieee_754.c` file utilizes bitwise operations to extract:
  - Sign bit
  - Exponent
  - Mantissa
- The extracted components are then printed in a readable binary format.

## Expected Output Example
For input `5.75`:

### 32-bit Representation
```
Sign Bit: 0
Exponent: 10000001
Mantissa: 01110000000000000000000
Hence, the final result: 01000000101110000000000000000000
```

### 64-bit Representation
```
Sign Bit: 0
Exponent: 10000000001
Mantissa: 0111000000000000000000000000000000000000000000000000
Hence, the final result: 0100000000010111000000000000000000000000000000000000000000000000
```

## Conclusion
This project provides multiple methods for IEEE 754 floating-point conversion, including a pure mathematical approach, a structured method using Python libraries, and a C-based implementation using bitwise operations. These approaches help in understanding the internal representation of floating-point numbers in computing systems.

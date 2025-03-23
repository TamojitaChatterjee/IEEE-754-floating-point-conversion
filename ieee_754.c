#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

void printBinary(uint64_t num, int bits) {
    for (int i = bits - 1; i >= 0; i--) {
        printf("%lu", (num >> i) & 1);
        if (bits == 32 && i % 8 == 0 && i != 0) printf(" "); //add spaces for readability
        if (bits == 64 && i % 8 == 0 && i != 0) printf(" "); //add spaces for readability
    }
    printf("\n");
}

void floatToIEEE754_32(float num) {
    uint32_t bits = *((uint32_t*)&num);
    uint32_t sign = (bits >> 31) & 1;
    uint32_t exponent = (bits >> 23) & 0xFF;
    uint32_t mantissa = bits & 0x7FFFFF;

    printf("32-bit IEEE 754 Representation (Binary):\n");
    printf("Sign Bit: %u\n", sign);
    printf("Exponent: ");
    printBinary(exponent, 8);
    printf("Mantissa: ");
    printBinary(mantissa, 23);
    printf("Hence, the final result: ");
    printBinary(bits, 32);
}

void doubleToIEEE754_64(double num) {
    uint64_t bits = *((uint64_t*)&num);
    uint64_t sign = (bits >> 63) & 1;
    uint64_t exponent = (bits >> 52) & 0x7FF;
    uint64_t mantissa = bits & 0xFFFFFFFFFFFFF;

    printf("64-bit IEEE 754 Representation (Binary):\n");
    printf("Sign Bit: %lu\n", sign);
    printf("Exponent: ");
    printBinary(exponent, 11);
    printf("Mantissa: ");
    printBinary(mantissa, 52);
    printf("Hence, the final result: ");
    printBinary(bits, 64);
}

int main() {
    double num;
    int choice;

    printf("Enter a number: ");
    scanf("%lf", &num);

    printf("Choose representation:\n");
    printf("1. 32-bit\n");
    printf("2. 64-bit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    if (choice == 1) {
        floatToIEEE754_32((float)num);
    } else if (choice == 2) {
        doubleToIEEE754_64(num);
    } else {
        printf("Invalid choice.\n");
    }

    return 0;
}
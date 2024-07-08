# Renz Gabrinao
# 100324156
# CPSC2190
# June 21, 2024
# lab2.py


def decimalToBaseN(n, base):
    # divide n by base
    # get quotient and reminder,
    # store reminder to the right most digit of result
    # keep dividing quotient until 0
    x = n
    pos = 1
    res = 0
    while(x > 0):
        r = x % base
        res = res + (r * pos)

        x = x // base
        pos = pos * 10
    
    return res

def decimalToBaseNRecursive(n, base, res = 0, pos = 1):
    if(n == 0):
        return res

    r = n % base
    res = res + (r * pos)
    return decimalToBaseNRecursive((n // base), base, res, pos * 10)


if __name__ == "__main__":
    # do stuff
    decimal1 = 12345
    decimal2 = 678910
    decimal3 = 111213
    
    print(f"\nDecimal {decimal1} to base 2: {decimalToBaseN(decimal1, 2)}")
    print(f"Decimal {decimal1} to base 8: {decimalToBaseN(decimal1, 8)}\n")

    print(f"Decimal {decimal2} to base 2: {decimalToBaseN(decimal2, 2)}")
    print(f"Decimal {decimal2} to base 8: {decimalToBaseN(decimal2, 8)}\n")

    print(f"Decimal {decimal3} to base 2: {decimalToBaseN(decimal3, 2)}")
    print(f"Decimal {decimal3} to base 8: {decimalToBaseN(decimal3, 8)}\n")

    print(f"Recursive: Decimal {decimal1} to base 2 = {decimalToBaseNRecursive(decimal1, 2)}")
    print(f"Recursive: Decimal {decimal1} to base 8 = {decimalToBaseNRecursive(decimal1, 8)}\n")

    print(f"Recursive: Decimal {decimal2} to base 2 = {decimalToBaseNRecursive(decimal2, 2)}")
    print(f"Recursive: Decimal {decimal2} to base 8 = {decimalToBaseNRecursive(decimal2, 8)}\n")

    print(f"Recursive: Decimal {decimal3} to base 2 = {decimalToBaseNRecursive(decimal3, 2)}")
    print(f"Recursive: Decimal {decimal3} to base 8 = {decimalToBaseNRecursive(decimal3, 8)}\n")

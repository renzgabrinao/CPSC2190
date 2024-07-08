# Renz Gabrinao
# 100324156
# CPSC 2190
# Lab 7
# July 4, 2024

# checks if x is a prime
#
# def: a prime number is a natural number
#      greater than 1 that has no positive
#      divisors other than 1 and itself
#
# time complexity: O(n)
def checkIfPrime(x):
    if(x < 2):
        return False

    for i in range(2, x): #range [2, x)
        if((x % i) == 0):
            return False

    return True

if __name__ == "__main__":

    flag = True

    while(flag):
        num = int(input("\nEnter an integer greater than 1: "))

        if(checkIfPrime(num)):
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")

        if(input("\nContinue? Enter 'y' for yes: ").lower() != "y"):
            flag = False;


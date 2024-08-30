# Renz Gabrinao
# 100324156
# CPSC 2190
# Lab 8
# July 11, 2024

def getPermutation(block):
    permutation = {}
    print(f"\nenter original permutation of the set.\npermutation must be in the set from [1 to {block}].")
    
    for i in range(0, int(block)):
        flag = True

        while(flag):
            num = int(input(f"o({i + 1}) = "))
            if num < 1 or num > block:
                print(f"invalid range. enter a number between [1 and {block}]")
            elif num in permutation.values():
                print(f"{num} is a duplicate and has already been used. enter a unique number.")
            else:
                permutation[i + 1] = num
                flag = False

    return permutation

def getInversePermutation(block):
    permutation = getPermutation(block)
    inverse = {}
    for val in permutation:
        inverse[permutation[val]] = val 

    return inverse

    
def encrypt(block, msg, permutation):  
    encrypted = ""
    for i in range(0, len(msg), block):
        currentBlock = msg[i : i + block]
        resultBlock = [None] * block
        
        for j in range(0, len(currentBlock)):
            finalIndex = int(permutation[j + 1]) - 1
            resultBlock[finalIndex] = currentBlock[j]

        res = "".join(resultBlock)
        encrypted += res
    
    return encrypted.upper()


if __name__ == "__main__":
    flag = True

    while(flag):
        choice = int(input("\nwould you like to encrypt or decrypt a message?\npress 1 for encrypt, 2 for decrypt.\n"))
        block = int(input("\nenter block size: "))
        msg = input("\nenter message to encrypt.\nall characters must be letters:\n")
       
        if(len(msg) % block == 0 and msg.isalpha() and (1 <= choice <= 2)):
            permutation = {}
            
            if(choice == 1):
                # encrypt 
                permutation = getPermutation(block)
               
            elif(choice == 2):
                # decrypt
                permutation = getInversePermutation(block)

            res = encrypt(block, msg, permutation) 
            print(f"\nFinal Message:\n\n\t{res}")

        else:
            print("\ninvalid message length, or the message contains non-alphabetic characters, or invalid choice.\ntry again.")
        
        flag = input("\nenter 'y' to continue.\n").lower() == 'y'

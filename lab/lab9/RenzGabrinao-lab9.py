# Renz Gabrinao
# 100324156
# CPSC 2190
# Lab 9
# July 18, 2024

def getChoice():
    choice = 0
    while(choice != 1 and choice != 2):
        choice = int(input("\nwould you like to encrypt or decrypt a message?\npress 1 for encrypt, 2 for decrypt.\n"))
        if(choice != 1 and choice != 2):
            print("invalid input. try again.")

    return choice;

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

    print("\ninverse of the permutation:")
    for val in permutation:
        print(f"o^-1({permutation[val]}): {val}")

    return inverse

    
def transmuteMessage(block, msg, choice):
    permutation = getPermutation(block) if choice == 1 else getInversePermutation(block)
    finalMsg = ""
    for i in range(0, len(msg), block):
        currentBlock = msg[i : i + block]
        resultBlock = [None] * block
        
        for j in range(0, len(currentBlock)):
            finalIndex = int(permutation[j + 1]) - 1
            resultBlock[finalIndex] = currentBlock[j]

        finalMsg += "".join(resultBlock)

    transmuteType = "ENCRYPTED" if choice == 1 else "DECRYPTED"
        
    print(f"\n{transmuteType} MESSAGE:\n\n\t{finalMsg.upper()}")
    

if __name__ == "__main__":
    flag = True;

    while(flag):
        choice = getChoice()
        block = int(input("\nenter block size: "))
        msg = input("\nenter message to encrypt.\nall characters must be letters:\n")
       
        if(len(msg) % block == 0 and msg.isalpha()):
            transmuteMessage(block, msg, choice) 

        else:
            print("\ninvalid message length, or the message contains non-alphabetic characters.\ntry again.")
        
        flag = input("\nenter 'y' to continue.\n").lower() == 'y'

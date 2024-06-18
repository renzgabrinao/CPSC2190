# binary search

def binarySearch(nums, target):
    left = 0
    right = len(nums)

    while(left < right):
        middle = int((left + right) / 2)
        
        if(target < nums[middle]):
            right = middle
        elif(target > nums[middle]):
            left = middle + 1
        else:
            return middle

    return -1

if(__name__ == "__main__"):

    nums = [1, 3, 5, 8, 9, 10, 14, 27, 34, 56, 78, 99, 120]
    print(binarySearch(nums, int(input())))
    





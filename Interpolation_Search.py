# Definition:Interpolation Search is a variant of Binary Search that 
# estimates the position of the target based on
# its value relative to the values in the sorted array.

# Real-life Analogy:Think of looking for a word in a dictionary. 
# You don’t start at the middle — you estimate based on the word's alphabetical position.

# Precondition:Data must be sorted and uniformly distributed.

# def inter_search(arr,target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high and arr[low] <= target <= arr[high]:
#         if low == high:
#             if arr[low] == target:
#                 return low
#             return -1
        
#         pos = low + ((high - low) * (target - arr[low]) // (arr[high] - arr[low]))

#         if arr[pos] == target:
#             return pos
#         elif arr[pos] < target:
#             low = pos + 1
#         else:
#             high = pos - 1
#     return -1

# arr = [1,2,3,4,5,6,7,8,9]
# target = 7

# ind = inter_search(arr,target)

# if ind != -1:
#     print("element at index:",ind)
# else:
#     print("element not found!")

def int_search(arr,target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        pos = low + ((high - low) * (target - arr[low]) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

arr = [2,3,4,5,6]
target = 4
ans = int_search(arr,target)

if ans != -1:
    print("element is found at index:",ans)
else:
    print("not found!!!!")



def iterative_search(arr,target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            low = mid + 1
        
        else:
            high = mid - 1
    return -1

# arr = [3,4,5,6,7,8]
# target = int(input("Enter the element target : "))

# result = iterative_search(arr, target)

# if result != -1:
#     print("element found at index",result)
# else:
#     print("element now found:")


# def recurssive_search(arr,target,low,high):
#     if low > high:
#         return -1
    
#     mid = (low + high) // 2

#     if arr[mid] == target:
#         return mid
    
#     elif arr[mid] < target:
#         return recurssive_search(arr,target,mid + 1,high)
    
#     else:
#        return  recurssive_search(arr,target,low,mid - 1)

# arr = [1,2,3,4,5,6,7,8]
# target = 3

# result = recurssive_search(arr,target,0,len(arr) - 1 )

# if target != -1:
#     print("element at index :",result)
# else:
#     print("element not found:")
    
# print("// program complete //")


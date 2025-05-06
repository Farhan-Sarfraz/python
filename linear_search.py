# arr = [88,45,3,2,6,34,1,0]
# target = int(input("enetr the target element : "))

# def unordered_search(arr,target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# print(unordered_search(arr,target))

# arr = [1,4,2,8,5]
# tar = int(input("enter the target elemet :"))

# def searching(arr,tar):
#     for i in range(len(arr)):
#      if arr[i] == tar:
#         return i
    
#     return -1

# print(searching(arr,tar))
    

arr = [1,2,3,4,5,6,7,8,9]
target = int(input("enter the target element : "))

def ordered_searching(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        else:
            if arr[i] > target:
                break
    return -1

value = ordered_searching(arr,target)
print(value)
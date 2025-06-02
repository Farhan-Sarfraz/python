

# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j = i - 1

#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1

#         arr[j + 1] = key
# arr = [4,5,3]
# insertion_sort(arr)
# print(arr)

# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j = i - 1

#         while j>= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key

# arr= [6,4,7]
# insertion_sort(arr)
# print(arr)

def ins_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key
arr = [8,7,3,9,2,0,1]
ins_sort(arr)
print("sorted array:->>>",arr)
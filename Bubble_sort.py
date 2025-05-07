# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
# arr = [3,9,5,4,7,1]
# bubble_sort(arr)
# print("sorted array :",arr)

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
# arr = [88,45,28,90,67,89,23,0,1,58]
# bubble_sort(arr)
# print("sorted array ->>>>",arr)

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

# arr = [1, 2, 3, 4, 5]
# bubble_sort(arr)
# print("Sorted array is:", arr)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [8,6,5,4,3,2,1]
bubble_sort(arr)
print("Sorted array is:", arr)

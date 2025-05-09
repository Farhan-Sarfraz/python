# def part(arr, first,last):
#     pi = arr[first]
#     left = first + 1
#     right=last

#     done = False
#     while not done:
#         while left <= right and arr[left] <= pi:
#             left = left  + 1
#         while right >= left and arr[right] >= pi:
#             right = right - 1
#         if right < left:
#             done  = True
#         else:
#             arr[left],arr[right] = arr[right],arr[left]
#     arr[first],arr[right]=arr[right],arr[first]
#     return right

# def quick_sort(arr,first,last):
#     if first < last:
#         split_point = part(arr,first,last)
#         quick_sort(arr,first,split_point - 1)
#         quick_sort(arr,split_point + 1,last)
# arr = [10, 7, 8, 9, 1, 5]
# quick_sort(arr,0,len(arr) - 1)
# print("sorted array:--->>>>", arr)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

arr = [15, 3, 2, 1, 9, 5, 7, 8, 6]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:-->>>", arr)

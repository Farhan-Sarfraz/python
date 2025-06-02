# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr

# arr = [64, 34, 25, 12, 22, 11, 90]
# print(bubble_sort(arr))


# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
# #         j = i - 1
# #         while j >= 0 and arr[j] > key:
# #             arr[j + 1] = arr[j]
# #             j -= 1
# #         arr[j + 1] = key
# #     return arr

# # arr = [12, 11, 13, 5, 6]
# # print(insertion_sort(arr))

# # def selection_sort(arr):
# #     for i in range(len(arr)):
# #         min_idx = i
# #         for j in range(i + 1, len(arr)):
# #             if arr[j] < arr[min_idx]:
# #                 min_idx = j
# #         arr[i], arr[min_idx] = arr[min_idx], arr[i]
# #     return arr

# # arr = [64, 25, 12, 22, 11]
# # print(selection_sort(arr))
# # def quick_sort(arr):
# #     if len(arr) <= 1:
# #         return arr
# #     pivot = arr[0]
# #     left = [x for x in arr[1:] if x < pivot]
# #     right = [x for x in arr[1:] if x >= pivot]
# #     return quick_sort(left) + [pivot] + quick_sort(right)

# # arr = [10, 7, 8, 9, 1, 5]
# # print(quick_sort(arr))
# def heapify(arr, n, i):
#     largest = i
#     l, r = 2*i + 1, 2*i + 2
#     if l < n and arr[l] > arr[largest]:
#         largest = l
#     if r < n and arr[r] > arr[largest]:
#         largest = r
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)

# def heap_sort(arr):
#     n = len(arr)
#     for i in range(n//2 - 1, -1, -1):
#         heapify(arr, n, i)
#     for i in range(n - 1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         heapify(arr, i, 0)
#     return arr

# arr = [12, 11, 13, 5, 6, 7]
# print(heap_sort(arr))


# def bubble_sort_modified(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         swapped = False
#         for j in range(n - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr

# arr = [1, 2, 3, 4, 5]
# print(bubble_sort_modified(arr))

# def insertion_sort_print(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#         print(arr)
#     return arr

# arr = [12, 11, 13, 5, 6]
# insertion_sort_print(arr)

# def selection_sort_count_swaps(arr):
#     swap_count = 0
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         if i != min_idx:
#             arr[i], arr[min_idx] = arr[min_idx], arr[i]
#             swap_count += 1
#     print("Total Swaps:", swap_count)
#     return arr

# arr = [64, 25, 12, 22, 11]
# selection_sort_count_swaps(arr)


# def linear_search(arr, key):
#     for i in range(len(arr)):
#         if arr[i] == key:
#             return i
#     return -1

# arr = [40, 20, 60, 10, 80]
# key = 60
# print("Element found at index:", linear_search(arr, key))

# def ordered_linear_search(arr, key):
#     for i in range(len(arr)):
#         if arr[i] == key:
#             return i
#         elif arr[i] > key:
#             return -1
#     return -1

# arr = [10, 20, 30, 40, 50]
# key = 30
# print("Element found at index:", ordered_linear_search(arr, key))

# def binary_search(arr, key):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == key:
#             return mid
#         elif arr[mid] < key:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# arr = [10, 20, 30, 40, 50]
# key = 40
# print("Element found at index:", binary_search(arr, key))


# def binary_search_recursive(arr, left, right, key):
#     if left > right:
#         return -1
#     mid = (left + right) // 2
#     if arr[mid] == key:
#         return mid
#     elif arr[mid] < key:
#         return binary_search_recursive(arr, mid + 1, right, key)
#     else:
#         return binary_search_recursive(arr, left, mid - 1, key)

# arr = [10, 20, 30, 40, 50]
# key = 40
# print("Element found at index:", binary_search_recursive(arr, 0, len(arr)-1, key))

# def linear_search_strings(arr, key):
#     for i in range(len(arr)):
#         if arr[i] == key:
#             return i
#     return -1

# arr = ["Alice", "Bob", "Charlie", "David"]
# key = "Charlie"
# print("Element found at index:", linear_search_strings(arr, key))


# def binary_search_bool(arr, key):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == key:
#             return True
#         elif arr[mid] < key:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return False

# arr = [10, 20, 30, 40, 50]
# key = 40
# print(binary_search_bool(arr, key))




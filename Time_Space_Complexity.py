# def get_first_num(arr):
#     return arr[0]

# arr = [2,3,4,5,6]
# element = get_first_num(arr)
# print("First element in the array is:",element)

# def access_element(arr):
#     return arr[3]

# arr = [3,4,5,7,8]
# print("ELEMENT IS :",access_element(arr))

# def print_element(arr):
#     for i in arr:
#         print(i)

# arr = [2,3,4,5,6,8]
# print_element(arr)

# def print_all_pairs(arr):
#     for i in arr:
#         for j in arr:
#             print(f"({i},{j})")

# arr = [1,2,3]
# print_all_pairs(arr)

# def copy_array(arr):
#     new_arr = []

#     for i in arr:
#         new_arr.append(i)
#     return new_arr

# arr = [1,2,3,4]
# print(arr)
# copied = copy_array(arr)
# print("copied array is:",copied)

# def binary_search(arr,key):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if arr[mid] == key:
#             return True
#         elif arr[mid] < key:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return False

# arr = [2,3,4,5,6]
# print("Binary search is:",binary_search(arr,4))

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array:", arr)

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         mid_idx = i
#         for j in range(i+1,n):
#             if arr[j] < arr[mid_idx]:
#                 mid_idx = j
        
#         arr[i] , arr[mid_idx] = arr[mid_idx] , arr[i]
# arr = [64, 25, 12, 22, 11]
# selection_sort(arr)
# print("Sorted array is:", arr)      

def slc_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i] , arr[min_idx] =arr[min_idx], arr[j]

arr = [78,43,90,8723,5632,219]
slc_sort(arr)
print(arr)
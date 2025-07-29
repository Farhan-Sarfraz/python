# day = 5

# match day:
#     case 1:
#         print("monday")
#     case 2:
#         print("tuesday")
#     case 3:
#         print("wednesday")
#     case 4:
#         print("thursday")
#     case 5:
#         print("friday")
#     case _:
#         print("invalid choice. ")

# point  = (0, 5)
# match point:
#     case (0, 0):
#         print("origin")
#     case (0, y):
#         print(f"y-axis : {y}")
#     case (x, 0):
#         print(f"x-axis : {x}")
#     case (x, y):
#         print(f"y-axis : {x},{y}")
    

def list_num(lst):
    match lst:
        case []:
            print("The list is empty.")
        case [x]:
            print(f"Single element list: {x}")
        case [x, y]:
            print(f"Two elements: {x} and {y}")
        case _:
            print(f"List with {len(lst)} elements: {lst}")


list_num([])
list_num([10])
list_num([1, 2])
list_num([1, 2, 3, 4])


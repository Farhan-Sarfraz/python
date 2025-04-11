# def fun_name(a,b):
#     sum=a+b
#     print(sum)
#     return sum
# fun_name(2,3)
# fun_name(4,65)

# def avr_num(a,b,c):
#     value=(a+b+c)/3
#     print(value)
#     return value
# avr_num(2.03,1.46,2.88)

# print("hello",end=" ")
# print("world")


# concepts of defualts parameters 
# def prod(a=1,b=2):
#     p=a*b
#     print(p)
#     return p
# prod()

# num=[1,2,3,4,5,6,7,8]

# def print_len(num):
#     print(len(num))
#     return len(num)
# print_len(num)

# touple = ("pak","ind","aus")

# def print_len(touple):
#     print(len(touple))

#     return len(touple)

# print_len(touple)

# touple = ("pak","ind","aus")

# def print_len(touple):
#     for item in touple:
#         print(item,end=" ")
# print_len(touple)

# list = [1,2,3,4,5,6,7,8,9,00]

# def print_list(list):
#     for p in list:
#         print(p,end=" ")
# print_list(list)


# def print_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#         print(fact)  
# print_fact(5)

# def currnecy(usdt):
#     pkr = usdt * 300

#     print(usdt," usdt =",pkr ," pkr")
# currnecy(2)

# def currency(pkr):
#     usdt = pkr/280
#     print(pkr , " pkr ",usdt, " usdt")
# currency(2800)

# def check(n):
#     if(n%2 == 0):
#         print("even")
#     else:
#         print("odd")
#         return n
# check(3)

# def find_max(arr):
#     if not arr:
#         return None
#     max_val = arr[0]
#     for num in arr:
#         if num > max_val:
#             max_val = num
#     return max_val

# # Test
# print(find_max([3, 7, 2, 9, 5]))  # Output: 9

# val = [2,3,4,5,6,7,8]
# def print_len(list):
#     print(len(list))
# print_len(val)

# val = [2,3,4,5,6,7,8]

# def print_list(list):
#     for item in list:
#         print(item,end=" ")
# print_list(val)

def checking(n):
    if n%2 == 0:
        print("number is even.")
    else:
        print("number is odd.")

n = int(input("enter the number :"))
ans = checking(n)
print(ans)
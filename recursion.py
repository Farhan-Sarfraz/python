
# def num(n):
#     if(n==0):
#         return 
#     print(n)
#     num(n-1)
# num(5)

# def num(n):
#     # if(n==0):
#     #     return 
#     print(n)
#     num(n-1)
# num(5)

# def fact(n):
#     # base case
#     if(n==1 or n==0 ):
#         return 1
#     # recursive case
#     return fact(n-1) * n 

# print(fact(3))

# def fact(n):
#     if( n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n
# print(fact(7))

# def cal(n):
#     if( n == 0 ):
#         return 0
#     return cal(n-1) + n
# sum=(cal(5))
# print(sum)

# def print_list(list,idx=0):
#     if(idx==len(list)):
#         return
#     print(list[idx])
#     print(list,idx+1)
# number = ["aus","pak","cina count"]
# print_list(number)
    
# def value(n):
#     if(n == 0):
#         return
#     print(n)
#     value(n-1)

# value(7)

# def fact(n):
#     if(n==0 or n== 1):
#         return 1
#     return n * fact(n-1)
# print(fact(3))
# print(fact(5))
# print(fact(10))
# print(fact(23))

# def calSum(n):
#     if( n == 0):
#         return 0
#     return calSum(n-1) + n

# sum=calSum(5)
# print(sum)

# def print_list(list,idx=0):
#     if(idx == len(list)):
#         return 
    
#     print(list[idx])
#     print_list(list,idx+1)

# vl = [2,3,5,6,7,9,0]

# print_list(vl)

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))
    
# def sum(n):
#     if n == 0:
#         return 0
#     return sum(n-1) + n
# print("sum is ",sum(5))


# def fabnocci(n):
#     if n <= 1:
#         return n
#     return fabnocci(n-1) + fabnocci(n - 2)
# for i in range(10):
#     print(fabnocci(i), end=" ")
    
# def reverse_string(str):
#     if str == "":
#         return str
#     return reverse_string(str[1:]) + str[0]
# reverse_string = reverse_string("pakistan")
# print(reverse_string)

def power_of_num(base, exp):
    if exp == 0:
        return 1
    return base * power_of_num(base, exp - 1)
print(power_of_num(2, 5))
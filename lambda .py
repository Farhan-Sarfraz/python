# add =  lambda x, y: x + y
# print(add(3,5))

# sub = lambda x, y: x - y
# print(sub(5,2))

# data = [(1,3),(2,2),(3,1),(3,2)]
# sorted_data = sorted(data,key=lambda x: x[1])
# print(sorted_data)

# num = [1,2,3,4,5]
# squares = list(map(lambda x: x**2,num))
# print(squares)

# number = (4,5,6,7)
# squares = tuple(map(lambda x: x**2,number))
# print(squares)

# square = lambda x: x * x
# print(square(5))   

# students = [("ali",89),("ham",67),("taha",90)]
# sorted_students = sorted(students,key=lambda x: x[1])
# print(sorted_students)

# is_even = lambda x: x % 2 == 0
# print(is_even(5))

# num = [12,3,4]
# sq = list(map(lambda x:x**2,num))
# print(sq)

# even =[1,2,3,4,5,6,7]
# even_num=list(filter(lambda x: x%2 == 0,even))
# print(even_num)

# words = ['python','java','c++','deep']
# upper_case=list(map(lambda x: x.upper(),words))
# print(upper_case)

# word =['LOVE','YOU']
# lower_case=list(map(lambda x: x.lower(),word))
# print(lower_case)

# num = [1,2,3]
# m = list(map(lambda x: x * 10 , num))
# print(m)

# combine = lambda first, last: first + "" + last 
# print(combine("com","bine"))

# maxi = lambda a,b: a if a > b else b
# print(maxi(23,44))

# words = ['word','meaning']
# len = list(map(lambda x: len(x),words))
# print(len)


# num = [4,5,6,7,8]
# odd_num = list(filter(lambda x: x %2 != 0,num))
# print(odd_num)

# employees = [
#     {"name" : "ali", "salery" : 5000},
#     {"name" : "charlie","salery": 3000},
#     {"name" : "bob" , "salery" : 9000},
# ]
# sorted_emp = sorted(employees,key=lambda x:x['salery'])
# print(sorted_emp)

# price = [100,200,900,800,700]
# rate_tax = 4
# price_with_tax = list(map(lambda x: x + (x * rate_tax),price))
# print(price_with_tax)

# products = [
#     {"name": "Laptop", "price": 1000},
#     {"name": "Phone", "price": 600},
#     {"name": "Tablet", "price": 400}
# ]
# most_expensive = max(products, key=lambda x: x['price'])
# print(most_expensive) 
# least_expensive = min(products, key=lambda x: x['price'])
# print(least_expensive) 

response = [
    {"user": "Alice", "age": 25, "city": "New York"},
    {"user": "Bob", "age": 30, "city": "Los Angeles"},
    {"user": "Charlie", "age": 35, "city": "Chicago"}
]

users = list(map(lambda x: x['user'], response))
print(users)  

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

sum_of_evens = sum(map(lambda x: x if x % 2 == 0 else 0, numbers))
print(sum_of_evens) 

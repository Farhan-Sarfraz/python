#  python haven't do while llop but we can simulate using while true and using break.

# while True:
#     num = int(input("enter the positive number. "))
#     print(f"your number is {num}")
#     if num < 0:
#         break


# correct_password = "python234"
# while True:
#     pwd = input("entered the password. ")
#     if pwd == correct_password:
#         print(f"password granted!, {pwd}")
#         break
#     print("invalid password, try again. ")
    

# i = 1

# while True:
#     print(i)
#     i += 1

#     if i > 5:
#         break



sum = 0
while True:
    num = int(input("enter the num. "))
    if num == 0:
        break
    sum += num
    print("total", sum)

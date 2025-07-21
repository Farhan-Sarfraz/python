# enemy = 1

# def increase_enemies():
#     enemy = 2
#     print(f"inside function : {enemy}")
# increase_enemies()
# print(f"after calling function : {enemy}")

#  global scope

# player = 11

# def player_team():
#     print(player)

# player_team()

#  local scope

# def number():
#     numbring = 11
#     print(numbring)

# number()
# print(numbering)


#  Enclosing Scope


# z = 30
# def outer_fun():
#     x = 20
#     def inner_fun():
#         y = 0
#         print(x)
#         print(y)
#         print(z)
#     inner_fun()
# outer_fun()

# game_level = 3
# def enemy_level():
#     enemies = [ "skeleton" , "alein" , "zombei"]

#     if game_level < 5:
#         new_enemy = enemies[0]
#     print(new_enemy)
# enemy_level()


# enemeis = 3

# def enemy_num():
#     global enemeis
#     enemeis += 1
#     print(f"inside function enemeis : {enemeis}")
# enemy_num()
# print(f"outside function enemeis : {enemeis}")


#  global scope should be used in constants

pi = 3.1415

def cal():
    global pi
    redius = 2
    return print(pi * redius)
cal()

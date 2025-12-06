# * args = allows you to pass multiple non-key arguments
# 1. positional, 2. default, 3. keyword, 4. arbitrary - we are here

# def add(*args): # * meaning we are using args yeah we can use random name there
#     total = 0 
#     for number in args:
#         total += number
#     return total 
# print(add(3,4,6,1,6,293))


def display_name(*biba): # args so useful when we dont know how many info we will get becuase it accept all our info and get into key
    for nick in biba:
        print(nick, end=" ")

display_name("danmg","yess i am ", "pipu")

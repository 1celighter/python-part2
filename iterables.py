# Iterables = an object/ collection that can return its element one at a time, 
# allowing it to be iterated over in a loop

numbers = [1,2,3,4,5]

for number in numbers:
    print(number)             # we just getting all our numbers from new lines

# we also can reverse it 

print()
print()
print()

for revnum in reversed(numbers):
    print(revnum) 

# we can do iterables with sets too but we cant reverse it we must know it otherwise we will get error if we want reverse it 

fruits = ("apple", "banana", "coconut","strawberry")

for fruit in fruits: # where i type fruit that mean a name of this iterable it can be any but in print we must type first name not second
    print(fruit) 

# for strings it also work too 

name = "Any name here"

for characters in name:
    print(characters, end=" ") # also , end="" in quots we can type any symbol and they will be print after 1 character 

print()
print()
# about dictionaries there we have a such differense 

# if we type it like string or smth we will get only key example is here

my_dictionary = {"A":1,"B":2,"C":3}

for key in my_dictionary:
    print(key)

# so if we need get only values we must write a buildin function near our dictionary that funct name is .values()
# example here 

for value in my_dictionary.values(): # () are must have to used othervise we will get error
    print(value) 

# but if we need type both we need just type a buildin funct .items()

for items in my_dictionary.items():
    print(items)

# and here we will get a both key and value but if we want delete from our answer this () we can type it like that

for key,value in my_dictionary.items():
    print(key,value)

# also we can format output however we want with fstrings 
# like that 
 
for key,value in my_dictionary.items():
    print(f"{key} = {value}") # likee that guys 
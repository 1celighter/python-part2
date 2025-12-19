# List comprehension = A concise way to create lists in Python
# Compact and easier to read than traditional loops
# [expression for value in iterable if condition]

# so now i will write a traditional while loop 

doubles = []

for x in range(1,11):
    doubles.append(x * 2)

print(doubles)

# but we can type it in less strings 

triple = [ x * 3 for x in range(1,11)] # yeah that make easier write a 7 to 12 line code

print(triple)

square = [x * 4 for x in range(1,11)]

print(square)

# well that all with numbers but what about strings?

# example hm we can pick capitalise 

fruits = ["apple", "banana", "orange", "coconut"]
fruits = [fruit.capitalize() for fruit in fruits]

# explaining [] in [ first we are saying what we want do.| for {object here for what object we want do it }.| in sets or tuples or whatever]

print(fruits)

# we also can a pick a letter from the string with this list comprehension 

fruits1 = ["dragonfruit", "lemon","lime","mango"]
fruits1_char = [fruit1[0] for fruit1 in fruits1]

print(fruits1_char)

# now conditions 

numbers = [1, 2, 3, 4, -5, 7, -10, 22, -12,]

positive_num = [num for num in numbers if num >=0]

negative_num = [num for num in numbers if num < 0]

print(positive_num)
print()
print(negative_num)

# here first word in [] meaning a return in our case need return a number with if in positive more than zero in negative less than zero

# we also can do it with division
 
print()

even_num = [num for num in numbers if num % 2 == 0 ]

odd_num = [num for num in numbers if num % 2 == 1]

print(even_num)
print()
print(odd_num)

# last example 

print()

grades = [69, 12, 39, 90, 70, 68, 99, 101]

passing_grades = [grade for grade in grades if grade >= 70]

print(passing_grades)
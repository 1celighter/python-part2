# module = a file containing code you want to include in your program 
# use 'import' to include a module (built-in or your own)
# useful to break up a large program reusable separate files

# okay right now we pick first if we need check some modules we can check it with help funcjust print it print(help('modules'))
# or check it directly like print(help('math'))

# well how we can use it = easy just type import and name module 

# using this modules too easy just type name ur module and module what u want to use clearly easy 

import math # that default method how to use it but also we can re name it for our cases 

import math as m # we must write as [any name for this module]
print(math.pi) # there we go 
print()
print(m.pi) # and we still get a pi number becasue we just re named it but module still a same 

print()
# but if we need only one or two specific things from one import we can text it like that 

from math import pi # BUT sometimes that was a bad because we can get a name conficts and we can get another results 

print(pi) # and we will still get our pi number

# about conflicts i mean like this 

from math import e 

a, b, c, e = 1, 2, 3, 4 
print(e ** a)
print(e ** b)
print(e ** c)
print(e ** e)

# but if i use import math and math.e in this example i will get another result and this will be right 

import math 

g, s, u, e = 1, 2, 3, 4
print(math.e ** g)
print(math.e ** s)
print(math.e ** u)
print(math.e ** e)

print()
print()
# there we go 

# now how to create ur own modules 

# now we need import our module just declare it 

import calcice 

result = calcice.pi
result1 = calcice.square(3)
result2 = calcice.cude(4)
result3 = calcice.circumference(10)
result4 = calcice.area(20)

print(result)

print()

print(result1)

print()

print(result2)

print()

print(result3)

print()

print(result4)

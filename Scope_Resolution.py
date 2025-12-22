# variable scope = where a variable is visible and accessible 
# scope resolution = this work in LEGB method we will accept our data in functions 
#  LEGB meaning = Local, Enclosed, Global, Build-in 

def func1():
    a = 1 
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2() 

# that a example for local resolution but if i want to change in print on funct 1 and 2 if i want to type first b and 2nd a i will get error
# that because our two functions a dont know about any data inside other func that a reasson why it named local and why we cant
# change a func like how i said in 16 line
# in two words function cant see inside of other functions 
# that all was is local func lets move to enclosed func

def func3():
    x = 1
    def func4():
        print(x)
    func4()
func3()

#  in this func we have a example of enclosed scope. this scope just gettin scope in our case that is x = 1 
# and just give it to another funct inside of func3 
# yeah litterally it just look like func3 give a func4 a x = 1 data to use it because we are using it inside function3 

# now global that is meaning outside of any functions like it 

d = 12 

def func5():
    print(d)
func5()

# that a fast example how global scope work we just declarate this scope and late we just using it = there evreything easy

# built-in scope 

from math import e 

def funcE():
    print(e)
funcE()

# this funct have a built in scope because its just got imported and we dont have any global local or enclosed declarated scope 
# but if we declarate e = 3 it is will be a global version and scope will be more on 3 because we declarated this scope and this scope is 3rd from 4 

# in our order we have local ALWAYS will be writen first secondary we have enclosed, 3rd we have a global and 4th we have a build in
# that a reasson why we will get a global result atleast build in 

def funcE1():
    print(e)

e = 3

funcE1()

# there we go 

# function that a block of reusable code
# place () after the function name to invoke it


# to definde a function we need write def and name it like
def congratulation():
    print("there is our congratulate")
    print("three times")
    print("acutallly")
    print()


congratulation()

# if we need invoke it three times we just do it like that

congratulation()
congratulation()
congratulation()

# but we got less information on this function we can get more with arguments


def happy_birthday(name):
    print(f"Happy birthday to {name}!")
    print()


happy_birthday("adam")  # here we are typing what we want get on 24 line and 25 line

# if we want add more we can just


def happy_birth(name, age):
    print(f"happy birthday {name}")
    print(f"you are {age} years old!")
    print(f"happy birthday to you!")


happy_birth("alexa", 21)
happy_birth("deny", 30)
happy_birth("bob", 19)


# example 1st / practice


def display_invoice(username, amount, due_date):
    print(f"hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")


display_invoice("Icelighter", 23.99, "1/01/2025")


# Return = statement used to end a function and sendd a result back to the caller


def add(x, y):
    z = x + y
    return z


def subtract(x, y):
    z = x - y
    return z


def multiply(x, y):
    z = x * y
    return z


def divine(x, y):
    z = x / y
    return z


print(add(3, 7))
print(subtract(9, 5))
print(multiply(4, 9))
print(divine(1245, 3))

# 2nd example


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("deny", "afton")
print(full_name)

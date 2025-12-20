# Match-case statement (switch): An alternative to using many 'elif' statements
# Execute some code if a value matches a 'case'
# Benefits: cleaner and syntax is more readable

# like this 

def day_of_week(day):
    if day == 1:
        return "This Sunday!"
    elif day == 2:
        return "This Monday!"
    elif day == 3:
        return "It is Tuesday!"
    elif day == 4:
        return "It is Wednesday!"
    elif day == 5:
        return "It is Thursday!"
    elif day == 6:
        return "It is Friday!"
    elif day == 7:
        return "It is Saturday"
    else:
        return "Not a valid day"
    
print(day_of_week(5)) # we can use any number to get any day from week but that so much code here

# we can do less code just use a match case like that 

def numbers(num):
    match num:
        case 1:
            return "This is case number 1"
        case 2:
            return "This is case number 2"
        case 3:
            return "This is case number 3"
        case 4:
            return "This is case number 4"
        case _:
            return "in this case _ meaning else just _ = wild card"
        
print(numbers(3))

# also there a how to work with booleans in cases 

def weekend(end):
    match end:
        case "Sunday!":
            return True
        case "Monday!":
            return False
        case "Tuesday":
            return False
        case "Wednesday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case "Saturday":
            return True
    
print(weekend("Saturday"))
# but code here so heavy isnt ig we need less code

def fruits(fruit):
    match fruit:
        case "apple" | "banana" | "coconut" | "orange":
            return "Yeah that all is fruit | True!"
        case "TV" | "Car" | "skateboard" | "pizza":
            return "that is not a fruit"
        
print(fruits("apple"))
print() # let check it all
print(fruits("TV"))

# | = this thing in match case meaning a word or apple or banana or coconut or orange that like example 
# well thats all i will come back tomorrow 
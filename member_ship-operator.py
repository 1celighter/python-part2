# membership operators = used to test whether a value or variable is found in a sequance 
# (string, list, tuples or dictionary)
# 1. in 
# 2. not in     

# there a programm for guessing letters 

word = "apple"

letter = input("Enter your guessing letter: ")

if letter in word:
    print(f"there is a {letter}")
else:
    print(f"we are not have a {letter}")

# btw there for string for list and tuples and sets i will type below 

students = ("patric", "sqize","john")

student = input("Enter a student to check: ")

if student in students:
    print(f"your student {student} is here!")
else:
    print(f"Your student {student} is not found!")

# Yeah for not in we just must change if and else statements and that all 

# but for dictionary we have a little differense to show result 

grades = {
    "Sandy": "A",
    "Squidward": "B",
    "Spongebob": "C",
    "Patric": "D"
}

student_grade = input("Enter name ur student to get he's grade: ")

if student_grade in grades:
    print(f"Your student {student_grade} have a {grades[student_grade]} grade!")
else:
    print(f"we are not have student with this {student_grade} name")

# for test this just we must check it on any projec like gmail verificator 

email = input("Enter ur email here: ")

if "@" in email and "." in email:
    print(f"{email} this email a valid!")
else:
    print(f"{email} this email is not a valid type a valid email.")
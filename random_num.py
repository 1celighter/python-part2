import random

low = 1
high = 100

rand = random.randint(low, high)

print(rand)

# that all random generate number principe

options = ("rock", "paper", "scissors")

rps = random.choice(options)

print(rps)

# that was for rock paper scissors

# also if we need random number from zero to 1 with floating number we can use random
floa = random.random()

print(floa)

# now we can do black jack cards game just for a example

cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# now we will make a game

low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = input(f"Enter a number between ({low} and {high}): ")
    guesses += 1

    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        print(f"{guess} is correct!")
    break

print(f"this round took you {guesses} guesses")

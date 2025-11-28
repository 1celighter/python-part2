import random

dice = []
total = 0
num_of_dice = int(input("how many dice?:"))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

print(dice)

for die in dice:
    total += die
print(f"total ur dice amount {total}")

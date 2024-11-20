import random

guess=int(input())
number=random.randint(1,10)
print("Welcome to the number guessing game, I'm thinking of a number between 1 and 10")
print("GO!")
if guess > number:
 print("OOPS! Too high, its hader than you think!")
elif guess < number:
 print("OOPS! Too low, its harder than you think")
else:
 print("GOOD JOB! I think you might be hacking but who cares! you win... absolutely NOTHING!")

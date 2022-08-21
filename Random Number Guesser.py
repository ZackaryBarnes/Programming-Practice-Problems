import random
import os
os.system("clear")

# Random Number Guesser problem from ProgrammingExpert.io

min_range = input("Enter the start of the range: ")
while not min_range.isdigit():
    print("Please enter a valid number.")
    min_range = input("Enter the start of the range: ")

max_range = input("Enter the end of the range: ")
while not max_range.isdigit() or int(max_range) < int(min_range):
    print("Please enter a valid number.")
    max_range = input("Enter the end of the range: ")

random_num = random.randint(int(min_range), int(max_range))

attempts = 0
guess = None

while guess != random_num:
    usr_guess = input("Guess a number: ")
    if not usr_guess.isdigit():
        print("Please enter a valid number.")
        continue

    attempts += 1
    guess = int(usr_guess)

suffix = ""
if attempts > 1:
    suffix = "s"

print(f"You guessed the number in {attempts} attempt{suffix}")



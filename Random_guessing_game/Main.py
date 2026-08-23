import random

print("Welcome to the Number Guessing Game! \nYou have 7 attempts to guess the number correctly.")

low = int(input("Enter the lower number of the range: "))
high = int(input("Enter the upper number of the range: "))

print(f"I'm thinking of a number between {low} and {high}. Can you guess what it is?")

num = random.randint(low, high)
#Total number of attempts
ch = 7
#Guessing counter   
gc = 0

while gc < ch:
    gc += 1
    guess = int(input(f"Enter your Guess: "))

    if guess == num:
        print(f"Congratulations! You've guessed the number {num} correctly in {gc} attempts!")
        break
    #this when the person guess the wrong number and the attempts are over
    elif guess >= ch and guess != num:
        print(f"Sorry! the number was {num}.Better luck next time!")
    #This is the when the person guesses the number too high or too low
    elif guess > num:
        print("Too high. Try a low number.")
    elif guess < num:
        print("Too low. Try a high number.")


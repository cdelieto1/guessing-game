"""A number-guessing game."""
import time

# Put your code here
from random import *

fname = input("What's ya name?: ")
print(f"{fname}, I'm thinking of a number between 1 and 100.") 

random_number=randint(1,100)
guess = int(input("Try to guess the numnber: "))

def guesstimaton(random_number):

	try:
		guess = int(random_number)
	except:
		print("please put in a valid number")		

	print('Drumroll....')
	time.sleep(2)
	print('... still thinking...')
	time.sleep(2)

	if guess > 100 or guess < 0:
		return "Number needs to be between 0 and 100, smartass!"
	elif guess==random_number:
		return "bingo!"
	elif random_number < guess:
		return "You're higher than the guess number"
	elif random_number > guess:
		return "You're lower than the guess number"
	else:
		return "Try playing again."

print(guesstimaton(random_number))		
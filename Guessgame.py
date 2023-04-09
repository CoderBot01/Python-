# Python-
Guess game using python 

import random
num = random.randint(1,20)
guess = int(input("Please guess the number: "))
while num != guess:
	if guess > num:
		print("your guess is high")
	else :
		print("your guess is low")
	guess = int(input("Guess again please:"))
print("your guess is correct ,the number is  ", guess)

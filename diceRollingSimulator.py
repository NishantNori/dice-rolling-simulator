from random import randint

minimumVal = 1
maximumVal = 6

rollDice = 'y'

while(rollDice == 'y'):
	print(randint(minimumVal, maximumVal))
	rollDice = input("Do you want to roll the dice? y/n")

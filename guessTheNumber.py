from random import randint

minVal = 1
maxVal = 6

randNum = randint(minVal, maxVal)
#print(randNum)


def isNumber(num):
	try:
		val = int(num)
		return True 
	except ValueError:
		return False	

enterString = input("Guess the number\n")

while True:
	if isNumber(enterString): #good input
		if (int(enterString) > randNum): #high guess
			print("You have guess a higher value\n")
			enterString = input("Guess the number\n")
		elif (int(enterString) < randNum): #low guess
			print("You have guessed a lower value\n")
			enterString = input("Guess the number\n")
		else: #correct guess
			print("You have guessed correctly!\n")
			break
	else: #bad input
		print("You have not entered a number!\n")
		enterString = input("Guess the number\n")








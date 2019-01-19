import random
gamewon=0
x = random.randrange(1, 100)
print("For this game you have 10 turns to answer the correct number")
for j in range(1,10+1):
	y = int(input("Please enter your guess: "))
	if y == x:
		print("You got the correct answer")
		gamewon=1
		break
	elif y < x:
		print("Your guess is too low")
		print("You have", 10-j,"turns left")
	else:
		print("Your guess is too high")
		print("You have", 10-j,"turns left")

if gamewon == 1:
	print ("you won")
else:
	print("you lose")
	print("the number was", x)




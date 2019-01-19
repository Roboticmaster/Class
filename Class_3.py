x = int(input("Please enter a number"))
y = x%2
if y==0:
	print("Your number", int(x), "is an even number")
else:
	print("your number", int(x), "is an odd number")




a = 25.2525
print("Your abs value of", (a), "is", int(abs(a)))
import math
print ("The ceiling output is", math.ceil(a))
print ("The floor output is", math.floor(a))




b = int(input("Please enter a number"))
c = int(input("please enter another number"))
print(math.pow(b, c))




import random
print ("random number is", random.randrange(1,200))




for x in range(1,10):
	print (x)




j = int(input("Please write a number"))
for y in range(1,j):
	print("hello", "This time it is", y)




l = int(input("enter a number"))
h=1
for f in range(1,l+1):
	h = h + f
	print (h)




l = int(input("enter a number"))
h=1
for f in range(1,l+1):
	h = h * f
	print (h)

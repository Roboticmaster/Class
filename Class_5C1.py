x=int(input("Please write a number"))
y=1
j=1
while (y<=x):
	j=j*y
	y=y+1
	if x == 0:
		print("your answer is 0")
	else:
		print("your answer is", j)
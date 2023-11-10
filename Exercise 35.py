humanage = int(input('Enter a human age:'))
if humanage < 0:
	print('Age must be positive number')	
elif (0 <= humanage <= 2):
	dogage = humanage * 10.5
else:
	dogage = 2*10.5 + (humanage - 2)*4
print('The dog age is', dogage)
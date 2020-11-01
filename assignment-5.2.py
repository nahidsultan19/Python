num = 0
largest = -1
smallest = None

while True:
	num = input('Enter a number: ')
	if num == 'done':
		break
	try:
		number =int(num)
	except:
		print('Invalid input')

	if smallest is None:
		smallest = number
	elif number < smallest:
		smallest = number
	elif number > largest:
		largest = number
print('Maximum is', largest)
print('Minimum is', smallest)
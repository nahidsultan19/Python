smallest = None

print('Before', smallest)
for value in [10, 41, 23, 3, 84, 16]:
	if smallest is None:
		smallest = value
	elif value < smallest:
		smallest = value

	print(smallest, value)
print('After', smallest)
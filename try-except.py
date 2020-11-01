rowstr = input('Enter Your Number: ')

try:
	ival = int(rowstr)
except:
	ival = -1

if ival > 0:
	print('Nice work')
else:
	print('Not a number')
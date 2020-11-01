hrs = input('Enter Hours: ')
rate = input('Enter Rate: ')
try:
	h = float(hrs)
	r = float(rate)
except:
	print('Error, Please enter correct value')
	quit()

if h > 40:
	regular = h * r
	overtime = (h - 40.0) * (r * 0.5)
	total = regular + overtime
else:
	total = h * r

print(total)
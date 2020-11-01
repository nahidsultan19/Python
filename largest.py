largest = -1
numbers = [5, 10, 50, 15, 20, 22]

for number in numbers:
    if number > largest:
        largest = number
    print(largest, number)

print('After', largest)

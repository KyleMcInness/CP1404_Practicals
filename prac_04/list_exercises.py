numbers = []

for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
numbers.sort()
print("The smallest numbers is {}".format(numbers[0]))
print("The largest number is {}".format(numbers[-1]))
average = 0
for i in numbers:
    average += i
average = average / 5
print("The average of the numbers is {}".format(average))

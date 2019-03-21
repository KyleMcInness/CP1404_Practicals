out_file = open("name.txt", 'w')

name = input("Name: ")
print(name, file=out_file)

out_file.close()

out_file = open("name.txt", "r")
print("Your name is {}".format(out_file.readline()))

out_file.close()

numbers = open("numbers.txt", "r")
result = 0
for line in numbers:
    result += int(line)
print(result)

numbers.close()

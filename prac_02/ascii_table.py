LOWER = 33
UPPER = 127

# 1
character = input("Enter a character: ")
ascii_code = ord(character)
print("The ASCII code for {} is {}".format(character, ascii_code))

# 2
ascii_code = int(input("Enter a number between 33 and 127: "))
while ascii_code < LOWER or ascii_code > UPPER:
    print("Enter a number greater than or equal to 33, or lower than or equal to 127")
    ascii_code = input("Enter a number between 33 and 127: ")
character = chr(ascii_code)
print("The character for {} is {}".format(ascii_code, character))

# 3
for i in range(LOWER, UPPER):
    print(i, chr(i))

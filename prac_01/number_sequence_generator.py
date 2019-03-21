x = int(input("Enter the first number: "))
while x < 0:
    x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
while x < 0:
    y = int(input("Enter the second number: "))

menu = input(
    'Would you like to see the (e)ven numbers, the (o)dd numbers, or the (s)quares? Or would you like to (q)uit?')

while menu != "q":
    # i
    if menu == "e":
        print("These are the even numbers between {} and {}".format(x, y))
        for i in range(x, y + 1):
            if i % 2 == 0:
                print(i, end=" ")
        print("")
    # ii
    elif menu == "o":
        print("These are the odd numbers between {} and {}".format(x, y))
        for i in range(x, y + 1):
            if i % 2 != 0:
                print(i, end=" ")
        print("")
    # iii
    elif menu == "s":
        print("These are the squares of the numbers between {} and {}".format(x, y))
        for i in range(x, y + 1):
            print(i**2, end=" ")
        print("")
    else:
        print("Invalid input")
    menu = input(
        'Would you like to see the (e)ven numbers, the (o)dd numbers, or the (s)quares? Or would you like to (q)uit?')
# iv
print("Finished.")

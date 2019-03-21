MENU = ("(H)ello\n"
        "(G)oodbye\n"
        "(Q)uit")

name = input("Enter name: ")
print(MENU)
menu_input = input("> ")

while menu_input != "Q":
    if menu_input == "H":
        print("Hello, {}".format(name))
    elif menu_input == "G":
        print("Goodbye, {}".format(name))
    else:
        print("Invalid input")
    print(MENU)
    menu_input = input("> ")

print("Finished.")

def main():
    MIN_LEN = 6

    password = get_password(MIN_LEN)

    convert_password(password)


def convert_password(password):
    print("*" * len(password))


def get_password(MIN_LEN):
    password = input("Enter password: ")
    while len(password) < MIN_LEN:
        print("Your password isn't long enough")
        password = input("Enter password: ")
    return password


main()


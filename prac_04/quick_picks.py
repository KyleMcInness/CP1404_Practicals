import random

MAXIMUM_LIST_LENGTH = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


def main():
    number_of_picks = int(input("How many quick picks? "))

    for i in range(number_of_picks):
        quick_picks = generate_quick_pick()
        print(
            "{:2} {:2} {:2} {:2} {:2} {:2}".format(*quick_picks))


def generate_quick_pick():
    numbers = []
    while len(numbers) < MAXIMUM_LIST_LENGTH:
        random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if random_number not in numbers:
            numbers.append(random_number)

    numbers.sort()
    return numbers


main()

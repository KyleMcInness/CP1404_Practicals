import random


def main():
    number_of_picks = int(input("How many quick picks? "))

    for i in range(number_of_picks):
        quick_picks = generate_quick_pick()
        print(
            "{:2} {:2} {:2} {:2} {:2} {:2}".format(*quick_picks))


def generate_quick_pick():
    numbers = []
    for index in range(6):
        random_number = random.randint(1, 45)
        if random_number not in numbers:
            numbers.append(random_number)
    numbers.sort()
    return numbers


main()

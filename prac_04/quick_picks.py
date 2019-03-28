import random

number_of_picks = int(input("How many quick picks? "))


def generate_quick_pick():
    numbers = []
    for index in range(6):
        numbers.append(random.randint(1, 45))
        numbers.sort()
    return numbers


for i in range(number_of_picks):
    quick_picks = generate_quick_pick()
    print(
        "{:2} {:2} {:2} {:2} {:2} {:2}".format(quick_picks[0], quick_picks[1], quick_picks[2], quick_picks[3],
                                               quick_picks[4], quick_picks[5]))

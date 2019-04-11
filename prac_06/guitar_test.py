from prac_06.guitar_class import Guitar

def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    g1 = Guitar(name, year, cost)
    print(g1)
    age_check = g1.get_age()
    print("{}: Expected {}, got {}".format(name, 2019-year, age_check))
    vintage_check = g1.is_vintage()
    print("{}: Expected {}, got {}".format(name, True, vintage_check))


main()
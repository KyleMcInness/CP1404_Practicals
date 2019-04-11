from prac_06.guitar_class import Guitar


def main():
    """"""

    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        g1 = Guitar(name, year, cost)
        guitars.append(g1)
        print(g1, "added.")
        name = input("Name: ")

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # guitars.append(Guitar("Fender Stratocaster", 1922, 765.4))

    for i, guitar in enumerate(guitars):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print("Guitar {}: {:19} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year,
                                                                 guitar.cost, vintage_string))


main()

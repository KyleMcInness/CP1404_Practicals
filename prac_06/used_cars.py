"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""

    # 1
    limo = Car(100, "Limo")
    # 2
    limo.add_fuel(20)
    # 3
    print("{} fuel = ".format(limo.name), limo.fuel)
    # 4
    limo.drive(115)
    # 5
    print("{} odo =".format(limo.name), limo.odometer)

    my_car = Car(180, "Car")

    my_car.drive(30)
    print("car fuel =", my_car.fuel)
    print("car odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))


main()

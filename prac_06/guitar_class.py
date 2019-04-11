class Guitar:
    """"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) :  ${:.2f}".format(self.name, self.year, self.cost)

    def __repr__(self):
        pass

    def get_age(self):
        age = 2019 - self.year
        return age

    def is_vintage(self):
        if 2019 - self.year >= 50:
            return True
        else:
            return False

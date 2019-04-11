class Students:
    """..."""

    def __init__(self, name="", student_number=0):
        self.name = name
        self.student_number = student_number

    def __str__(self):
        return "{} has the student number {}".format(self.name, self.student_number)

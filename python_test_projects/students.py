from python_test_projects.student import Students

MENU = "L, A, Q"


def main():
    students = []
    print(MENU)
    menu_choice = input("> ")
    while menu_choice.upper() != "Q":
        if menu_choice.upper() == "L":
            if len(students) > 0:
                for student in range(len(students)):
                    print("Student {}:".format(student + 1), students[student])
            else:
                print("No students have been added.")
        elif menu_choice.upper() == "A":
            add_student(students)
        else:
            print("Invalid menu input")
        print(MENU)
        menu_choice = input("> ")
    print("Goodbye")


def add_student(students):
    name = input("Name: ")
    stu_num = int(input("Student Number: "))

    students.append(Students(name, stu_num))

    return students


main()

""""""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """"""

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby)
    print(python)
    print(visual_basic)

    programming_languages = [["Ruby", "Dynamic", True, 1995], ["Python", "Dynamic", True, 1991],
                             ["Visual Basic", "Static", False, 1991]]

    print("The dynamically typed languages are:")

    for language in programming_languages:
        check_if_dynamic = ProgrammingLanguage(*language)
        if check_if_dynamic.is_dynamic():
            print(check_if_dynamic.language)


main()

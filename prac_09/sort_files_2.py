import shutil
import os


def main():
    os.chdir('FilesToSort2')

    extensions = [filename.split('.') for filename in os.listdir()]
    chosen_categories = []

    key_to_extension = {}

    for i, extension in enumerate(extensions):
        key_to_extension[extension[1]] = i

    for key in key_to_extension:
        choice = input("What category would you like to sort {} files into? ".format(key))
        chosen_categories.append(choice)
        try:
            os.mkdir('{}'.format(choice))
        except FileExistsError:
            pass
        for extension in extensions:
            if "{}".format(key) == extension[1]:
                shutil.move(extension[0] + '.' + extension[1], choice)


main()

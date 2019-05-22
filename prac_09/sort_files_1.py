import shutil
import os


def main():
    print("The current directory is {}".format(os.getcwd()))

    os.chdir('FilesToSort')

    extensions = [filename.split('.') for filename in os.listdir()]

    for extension in extensions:
        try:
            os.mkdir('{}'.format(extension[1]))
        except FileExistsError:
            pass
        shutil.move(extension[0] + "." + extension[1], extension[1])


main()

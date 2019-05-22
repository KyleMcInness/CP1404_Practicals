import shutil
import os


def main():
    print("The current directory is {}".format(os.getcwd()))

    os.chdir('FilesToSort')

    extensions = [filename.split('.') for filename in os.listdir()]

    for extension in extensions:
        print(extension[0] + "." + extension[1])
        print(extension[1])
        if not os.path.isdir(extension[1]):
            os.mkdir("{}".format(extension[1]))
        shutil.move(extension[0] + "." + extension[1], extension[1])


main()

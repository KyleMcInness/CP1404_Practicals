HEX_COLOURS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "BlanchedAlmond": "#ffebcd", "BlueViolet": "#8a2be2",
               "CadetBlue": "#5f9ea0", "chocolate": "#d2691e", "coral": "#ff7f50", "CornflowerBlue": "#6495ed",
               "firebrick": "#b22222", "GhostWhite": "#f8f8ff"}


colour_name = input("Enter a colour name: ")

while colour_name != "":
    if colour_name in HEX_COLOURS:
        print("{}'s hex value is {}".format(colour_name, HEX_COLOURS[colour_name]))
    else:
        print("That colour is not in our dictionary")
    colour_name = input("Enter a colour name: ")

COLOURS = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
           "Barn Red": "#7c0a02", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
           "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc"}
key = input("Enter colour:").title()
while key != "":
    if key in COLOURS:
        print(COLOURS[key])
    else:
        print("Invalid")
    key = input("Enter colour:").title()
print("Program Finished")

"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

all_sentences = ""
state_code = input("Enter short state: ").upper()
for i in CODE_TO_NAME:
    while state_code != "":
        try:
            sentence = f"{state_code} is {CODE_TO_NAME[state_code]}"
            print(sentence)
            all_sentences += sentence + "\n"
        except KeyError:
            print("Invalid")
        state_code = input("Enter short state: ").upper()

print(all_sentences)

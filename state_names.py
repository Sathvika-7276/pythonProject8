"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""
# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)
for key in CODE_TO_NAME:
    value = CODE_TO_NAME[key]
    print(f"{key} is {value}")

state_code = input("Enter short state: ").upper()
for i in CODE_TO_NAME:
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid")
    state_code = input("Enter short state: ").upper()

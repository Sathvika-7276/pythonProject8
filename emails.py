"""
Emails
Estimate: 30 minutes
Actual:   40 minutes
"""


def main():
    dictionary = {}
    email = input("Email:")
    while email != "":
        name = extract_name(email)
        name_check = input(f"Is your name {name}? (Y/n)")
        if name_check.upper() != "Y" and name_check != "":
            name = input("Name:")
        dictionary[email] = name
        email = input("Email:")
    print("\n")
    for email, name in dictionary.items():
        print(f"{name} ({email})")


def extract_name(email):
    separate = email.split("@")[0]
    split = separate.split(".")
    user_name = " ".join(split).title()
    return user_name


main()

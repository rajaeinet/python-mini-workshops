# Simple PhoneBook (Functional) - not Complete
# problem Solving Workshop (for beginner Programmers) - Online ShzU

# string  "", ''
# number int-float 5 7.3
# boolean
# list [15, 17, 19, 25, 19]

# key : value
# dictionary
# en2pr = { "hello":"سلام", "water":"آب" }

phonebook = {"omid":  "123",
             "negar": "456"}


def add(name, phone):
    # ex: if exists
    phonebook[name] = phone

def find(name):
    if name in phonebook:
        print(phonebook[name])  # or return
    else:
        print("not Found!")

def remove(name):
    # if exists or pop(name, None) - Search for alternative Solutions
    phonebook.pop(name)
    # print("Removed!")

# ex: edit PhoneBook Contact

add("ehsan", "789")
# add("omid", "000")  # Replaced if Exists
print(phonebook)


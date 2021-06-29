import json


def set_number():
    number = input(f"What are you lucky number? ")
    filename = 'number.json'
    with open(filename, 'w') as f:
        json.dump(number, f)
    return number


def say_number():
    number = set_number()
    print(f"Hey a know your lucky number it is {number}!")


say_number()

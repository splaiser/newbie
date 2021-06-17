print("Give me two numbers,and i'll plus them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst nubmer:")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)+int(second_number)
    except ValueError:
        print("Please don't use a word")
    else:
        print(answer)
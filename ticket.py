message = f'Hello do you want a ticket? if yes please tell me your age. '
message += f'\nEnter your age or if you dont want more a ticket send quit: '
age = ''
active = True
while active:
    age = input(message)
    if age == 'quit':
        break
    age = int(age)

    if age <= 3:
        print(f'For you ticket price 0')
    elif age <= 12:
        print(f'For you ticket price 10 dollars')
    elif age > 12:
        print(f'For you ticket price 15 dollars')
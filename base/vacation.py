vacations = {}
polling_active = True
while polling_active:
    name = input('\nWhat is your name? ')
    vacation = input('Where you like to go travel in this summer? ')
    vacations[name] = vacation

    repeat = input('Would you like to let another person says? yes or no: ')
    if repeat == 'no':
        polling_active = False
print('\n Congratulation you are finish the Poll ')
for name,vacation in vacations.items():
    print(f'{name} would like travel to {vacation}')
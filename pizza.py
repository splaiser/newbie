topings = f'What a toping you want to add to your pizza?'
topings += f'\nEnter name of toping to add or quit to finish your pizza: '
toping = ''
print(topings)
while toping != 'quit':
    toping = input()

    if toping != 'quit':
        print('something else?')

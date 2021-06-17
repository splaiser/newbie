filename =  'guest.txt'


while(True):
    with open(filename, 'r+') as file_object:
        mes = input('What is your name?: \n')
        text = file_object.readlines()
        file_object.write(f"\nHello {mes} ")


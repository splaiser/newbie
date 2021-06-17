def cats_and_dogs(filename):
    #при перемещении текстовых файлов с влюченным except выводиться сообщение о том, что файл недоступен.
    #При выключенным except файл просто пропускается, а функция продолжает работу
    try:
        with open(filename) as f:
            contents = f.read()

    except FileNotFoundError:
        #print("File not found!")
        pass
    else:
        print(contents)

filenames = ['dogs.txt', 'cats.txt']
for filename in filenames:
    cats_and_dogs(filename)
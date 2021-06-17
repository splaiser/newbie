def cats_and_dogs(filename):
    try:
        with open(filename) as f:
            contents = f.read()

    except FileNotFoundError:
        print("File not found!")
    else:
        print(contents)

filenames = ['dogs.txt', 'cats.txt']
for filename in filenames:
    cats_and_dogs(filename)
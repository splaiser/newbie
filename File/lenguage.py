filename = 'language_file.txt'


with open(filename) as file_object:
    lines = file_object.readlines()
result = [elem.replace("Python", "C") for elem in lines]
print(result)




lucky_number = {'nikita' : [13,6,18], 'sveta' : [8,12,11], 'valya' : [3,4,8], 'gena' : [7] }

for name,numbers in lucky_number.items():
    print(f"{name}s best number is:")
    for number in numbers:
        print(f"\t{number}")
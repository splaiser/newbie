from random import randint

class Dice():
    def __init__(self, sides=6 ):
        self.side = sides

    def roll_dice(self):
        result = randint(1,self.side)
        print(result)



roll_0= Dice()
roll_0.roll_dice()

for number in range(10):
    roll= Dice(10)
    roll.roll_dice()

for number in range(10):
    roll= Dice(20)
    roll.roll_dice()
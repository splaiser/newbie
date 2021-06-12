from random import choice

class Lottery():

    def __init__(self):
        self.list = [1,2,3,4,5,6,7,8,9,10,'q','w','e','r','t']


    def randomiser(self):
        result = []
        for n in range(4):

            random = choice(self.list)
            result.append(random)

        print(f"Congratulation winners with tikket {result}! ")

lottery_0 = Lottery()
lottery_0.randomiser()
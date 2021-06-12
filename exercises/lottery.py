from random import choice
# Создать список с 10ти цифр и 5ти букв. Сделать цикл который будет выбирать 4 случайных символа.
# Сравнить случайную комбинацию с одной удачной комбинацией и вывести количество необходимых попыток.
class Lottery():

    def __init__(self):
        self.list = [1,2,3,4,5,6,7,8,9,10,'q','w','e','r','t']


    def randomiser(self):
        score = 0
        happy_result = [7,7,7,'e']
        result = []
        while happy_result != result:
            result = []
            for n in range(4):
                random = choice(self.list)
                result.append(random)
            score = score + 1

        print(score)


lottery_0 = Lottery()
lottery_0.randomiser()
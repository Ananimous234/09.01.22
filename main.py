import random
class Myworld:
    def __init__(self):
        self.__name = random.randint(1, 9999)
        self.__bot = random.randint(1, 9999)
        print(f'? + ? = {self.__name + self.__bot}')
ff = Myworld()
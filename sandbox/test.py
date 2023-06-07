print('Hello World')


class Creature(object):
    def __init__(self, name=None):
        self.name = name
        print(f'The creature {self.name} is born now')


class Human(Creature):
    def __init__(self, name, sexual='female', tall=160):
        super().__init__(name)
        self.sexual = sexual
        self.tall = tall
        print(f'The human ({self.sexual}, {self.tall}) is born now')


class Dog(Creature):
    def __init__(self, name, sexual='female', tall=50):
        super().__init__(name)
        self.sexual = sexual
        self.tall = tall
        print(f'The dog ({self.sexual}, {self.tall}) is born now')


# main
# creature1 = Creature()
human1 = Human('human1')
dog1 = Dog('Dog1')

class Animal:
    exists: True

class liveBirthGiver(Animal):
    def __init__(self) -> None:
        pass
    
    isLiveBirth: True

class mammal(liveBirthGiver):
    def __init__(self, isLiveBirth, nurseYoung):
        self.isLiveBirth = isLiveBirth
        self.nurseYoung = nurseYoung
    
    def speak (self, sound):
        raise Exception('Speak is not defined!')

    nurseYoung: True

class reptile (liveBirthGiver):
    def __init__(self, isLiveBirth):
        self.isLiveBirth = isLiveBirth
        pass

class predator (mammal):
    def __init__(self):
        pass

    isPredator: True
    hasClaws: True
    hasTail: True


class canine(predator):
    # A method is a function that's inside of a class
    # A function is just a function.
    def __init__(self):
        pass


    def bark (self, sound):
        self.speak(sound)
    def speak (self, sound):
        print('Bark Bark', sound)

    hasCanineTeeth: True
    isQuadrapedal: True
    eatsOwnPoop: True

class feline(predator):
    def __init__(self):
        pass

class cat(feline):
    def __init__(self):
        self.meow

    def meow (self, sound):
        self.speak(sound)

    def speak (self, sound):
        print('MeOw MeOw ', sound)


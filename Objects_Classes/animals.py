class Dog:

    scientific_name = "Canis lupus familiaris"

    def __init__(self, name):
        self.name = name
        self.woofs = 0

    def do_trick(self):
        pass

    def count(self):
        self.woofs += 1
        for bark in range(self.woofs):
            self.speak()


    def speak(self):
        print("Woof!")

    def eat(self, food):
        if food == "biscuit":
            print("Yummy!")
        else:
            print("That's not food!")

    def hear(self, words):
        if self.name in words:
            self.speak()

class Chihuahua(Dog):
    origin = "Mexico"

    def speak(self):
        print("Yip!")

class Husky(Dog):
    origin = "Mexico"

    def speak(self):
        print("Awooooo!")

class Viejo_pastor_ingles():
    pass

class Labrador(Dog):
    origin = "Canada"


class TrainedChihuahua(Chihuahua):
    def do_trick(self):
        print("The chihuahua spins in the air and turns briefly into a chicken.")


class Cat:

    def __init__(self):
        self.mood = "neutral"

    def speak(self):
        if self.mood == "happy":
            print("Purrr!")
        elif self.mood == "angry":
            print("Hiss!")
        else:
            print("Meow!")

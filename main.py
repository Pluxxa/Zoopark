class Animal():
    def make_sound(self):
        return "Звуки животного!"


class Dog(Animal):
    def make_sound(self):
        return "woof!"


class Cat(Animal):
    def make_sound(self):
        return "meaw!"


class Cow(Animal):
    def make_sound(self):
        return "mooo!"


def sound(animal):
    print(animal.make_sound())


dog = Dog()
cat = Cat()
cow = Cow()

a = [dog, cow, cat]
for i in a:
    sound(i)
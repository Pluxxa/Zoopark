import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(name, age)
        self.can_fly = can_fly

    def make_sound(self):
        return "Chirp chirp"

    def eat(self):
        return "Seeds"


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Roar"

    def eat(self):
        return "Grass"


class Reptile(Animal):
    def __init__(self, name, age, scale_color):
        super().__init__(name, age)
        self.scale_color = scale_color

    def make_sound(self):
        return "Hiss"

    def eat(self):
        return "Insects"


def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)

    def save_zoo(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_zoo(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

class ZooKeeper:
    def __init__(self, name, age, experience):
        self.name = name
        self.age = age
        self.experience = experience

    def feed_animal(self, animal):
        return f"{self.name} is feeding {animal.name}"

    def __str__(self):
        return f"ZooKeeper: {self.name}, Age: {self.age}, Experience: {self.experience} years"


class Veterinarian:
    def __init__(self, name, age, specialty):
        self.name = name
        self.age = age
        self.specialty = specialty

    def heal_animal(self, animal):
        return f"{self.name} is healing {animal.name}"

    def __str__(self):
        return f"Veterinarian: {self.name}, Age: {self.age}, Specialty: {self.specialty}"



# Пример использования сохранения и загрузки данных о зоопарке
zoo = Zoo()
zoo.add_animal(Bird("Parrot", 3, True))
zoo.add_animal(Mammal("Tiger", 5, "Orange"))
zoo.add_animal(Reptile("Snake", 2, "Green"))
zoo.add_staff(ZooKeeper("John", 30, 5))
zoo.add_staff(Veterinarian("Alice", 35, "Surgery"))

# Сохраняем состояние зоопарка в файл
zoo.save_zoo('zoo_data.pickle')

# Загружаем состояние зоопарка из файла
loaded_zoo = Zoo.load_zoo('zoo_data.pickle')

# Печатаем информацию о загруженном зоопарке
print("Загруженные данные о зоопарке:")
for animal in loaded_zoo.animals:
    print(animal.name, animal.age)
for staff in loaded_zoo.staff:
    print(staff)

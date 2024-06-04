class Animal:
     def __init__(self, name, age):
         self.name = name
         self.age = age

     def eat (self):
        print(f"{self.name} is eating")
     def sleep (self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def eat(self):
        print(f'{self.name} is eating like a dog')

    def bark(self):
        print(f'{self.name} is barking')

class cat(Animal):
    def eat(self):
        print(f'{self.name} is eating like a cat')

    def purr(self):
        print(f'{self.name} is purring')

if __name__ == "__main__":
    dog = Dog('Kevin', 4)
    cat = cat('Siri', 3)

    dog.eat()
    dog.sleep()
    dog.bark()

    cat.eat()
    cat.sleep()
    cat.purr()

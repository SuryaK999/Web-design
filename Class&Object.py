class Animal:  #base class
    def speak(sound):
        return "Animal makes a sound"
class Dog(Animal):  #inheritence class
    def speak(sound):
        return "Bau Bau"
class Cat(Animal):   
    def speak(sound):
        return "Meow Meow"
class Cow(Animal):   
    def speak(sound):
        return "Ambaaa Ambaa"
dog,cat,cow= Dog(), Cat(), Cow()
print(dog.speak())
print(cat.speak())
print(cow.speak())

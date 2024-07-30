#single heritance
class Animal:
    def speak():
        return "Animal is speaking"
    #single heritance
class dog(Animal):
    def bark():
        return  "bow"
obj1=Animal
print(obj1.speak())
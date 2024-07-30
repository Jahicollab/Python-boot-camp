#we can give many classes in this method last in print what we given in a print statement
class Animal:
    def speak():
        return"Animal is speaking"
    #single inheritence
class dog(Animal):
    def bow():
        return "Bow"
class puppy(dog):
    def shout():
        return "i am child"
obj3=puppy
print(obj3.shout())


#o/p
#i am child
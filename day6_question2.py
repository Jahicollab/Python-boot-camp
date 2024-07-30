#creating a class
class Myclass:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
    def mod(a,b):
        return a%b
object1=Myclass
print(object1.add(12,4))
print(object1.sub(12,4))
print(object1.mul(12,4))
print(object1.div(12,4))
print(object1.mod(12,4))
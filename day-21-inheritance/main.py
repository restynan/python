# To inherit a class you just put the class in the  class brackets and the call super.__initi__()
class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("exhale , inhale")


class Fish(Animal):
    def __int__(self):
        super().__init__()

    def swim(self):
        print("fish can swim")

    def breathe(self):
        super().breathe()
        print("breathing under water")


fish = Fish()
fish.swim()
print(fish.eyes)
fish.breathe()

#list  slicing
piano_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

print(piano_keys[2:5])
print(piano_keys[4:])
print(piano_keys[:6])
#skip
print(piano_keys[2:8:2])
#reversing a list
print(piano_keys[::-1])

#loooping through  from the end of the list
list = [1,2,3,4,5,6,7,8,9]
for i in range(len(list)-1, 0, -1):
    print(list[i])
#print(list[::-1])


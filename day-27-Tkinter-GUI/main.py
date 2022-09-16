import tkinter

# https://docs.python.org/3/library/tkinter.html#the-packer
window = tkinter.Tk()
# opens the GUI and listens what the user will do

window.title("My first GUI Program")
window.minsize(width=500, height=500)

my_label = tkinter.Label(text="I am a label", font=("Arial", 25, "bold"))
# my_label.pack()
my_label.pack(side="left")


# window.mainloop()


# Advanced argument to specify a wider range of inputs
# unlimited arguments
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(f'Addition result: {add(1, 2, 7)}')


# kwargs
# takes a number add 5 and multiply by 3
def calculator(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


ans = calculator(2, add=5, multiply=3)
print(f'Result: {ans}')


# advantage of using get(on a dictionary if the value doesnot exist it return none), but when you use position
# arguments it breaks

class Car:
    def __init__(self, **kwargs):
        self.model = kwargs.get("model")
        self.make = kwargs.get("make")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("sets")


car1 = Car(make="Ford")
print(f'modal: {car1.model}')
print(f'make: {car1.make}')

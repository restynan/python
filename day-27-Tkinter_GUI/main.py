from tkinter import *

# https://docs.python.org/3/library/tkinter.html#the-packer

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#padding
window.config(padx=20, pady=20)

# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()
# label.place(x=50, y=5)
#label.grid(row=0, column=0)


# tkinter positioning pack, place, and grid
# if a widget is created without specifying pack, place or grid it willnot be shown
# pack -starts from the top and packs every other widget below the previous one, Hard to specify a specific position
# place - precise position, you can provide a X and Y value

# Buttons
def action():
    print("Do something")


# calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()
#label.grid(row=1, column=1)

# Entries
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.pack()
#entry.grid(row=2, column=2)

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()
#text.grid(row=3, column=3)


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()
#spinbox.grid(row=4, column=2)


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()


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


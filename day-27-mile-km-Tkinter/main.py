from tkinter import *

window = Tk()
window.title("Mile to km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

input_miles = Entry(width=10)
input_miles.grid(row=0, column=1)
input_miles.insert(END, 0)

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

label_equal = Label(text="is equal to")
label_equal.grid(row=1, column=0)

label_kilometer_result = Label(text="0")
label_kilometer_result.grid(row=1, column=1)

label_km = Label(text="Km")
label_km.grid(row=1, column=2)


def miles_to_km():
    miles = float(input_miles.get())
    km = round(miles * 1.609)
    label_kilometer_result.config(text=f"{km}")

button_calculate = Button(text="Calculate", command=miles_to_km)
button_calculate.grid(row=2, column=1)

window.mainloop()

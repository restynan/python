from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    random.shuffle(password_list)
    # join
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
    print(f"Your password is: {password}")


# ----------------------------search-----------------------------------------#
def find_password():
    website = website_input.get()
    try:
        with open("password.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \npassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website}  website found ")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    # create a json data
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="opps", message="please don't leave the fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f'These are the details you entered: \nEmail: {email} \npassword: {password} \nIs it ok to save?')
        if is_ok:

            try:
                with open("password.json", mode="r") as password_file:
                    # reading old data
                    data = json.load(password_file)
            except FileNotFoundError:
                with open("password.json", mode="w") as password_file:
                    json.dump(new_data, password_file, indent=4)
            else:
                # updating old data with new data
                data.update(new_data)
                with open("password.json", mode="w") as password_file:
                    # save updated data
                    json.dump(data, password_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# canvas
canvas = Canvas(width="200", height="200", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

search_button = Button(text="Search", width=11, command=find_password)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "resty@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=19)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password", width=11, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()

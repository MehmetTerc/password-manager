from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get().capitalize()
    email = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="EMPTY FIELD", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get().capitalize()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No data file found")
    else:
        if website in data:
            messagebox.showinfo(title=website,
                                message=f"Website: {data[website]["email"]} / Password: {data[website]["password"]}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for this {website} exist")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_Lbl = Label(text="Website: ")
website_Lbl.grid(column=0, row=1, sticky="W")  # Links ausgerichtet

user_Lbl = Label(text="Email/Username:  ")
user_Lbl.grid(column=0, row=2, sticky="W")  # Links ausgerichtet

passwort_Lbl = Label(text="Passwort: ")
passwort_Lbl.grid(column=0, row=3, sticky="W")  # Links ausgerichtet

# Entries
website_entry = Entry(width=30)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")  # Dehnt sich bei Bedarf aus
website_entry.focus()

user_entry = Entry(width=30)
user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
user_entry.insert(0, "memo@mail.com")

password_entry = Entry(width=15)
password_entry.grid(column=1, row=3, sticky="EW")  # Rechts ausgerichtet

# Buttons
passwordBtn = Button(text="Generate Password", width=15, command=generate_password)
passwordBtn.grid(column=2, row=3, sticky="W")  # Links vom Button-Zelle ausgerichtet

addBtn = Button(text="Add", width=33, command=save)
addBtn.grid(column=1, row=4, columnspan=2, sticky="EW")  # Mittig und dehnt sich

searchBtn = Button(text="Search", width=15, command=find_password)
searchBtn.grid(column=2, row=1, sticky="W")  # Mittig und dehnt sich

window.mainloop()

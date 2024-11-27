from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

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
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="EMPTY FIELD", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {user}"
                                                              f"\npassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website} | {user} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


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

window.mainloop()

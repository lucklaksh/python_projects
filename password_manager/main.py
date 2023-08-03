from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get().title()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        is_ok = False
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\nEmail:{email}\nPassword:{password}\nIs it OK to Save?")

    if is_ok:
        try:
            with open("data.json", mode='r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode='w') as data_file:
                json.dump(new_data, data_file)
        else:
            data.update(new_data)
            with open("data.json", mode='w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------WEBSITE PASSWORD GETTER-----------------------------#


def find_password():
    website = website_entry.get().title()
    try:
        with open("data.json", mode='r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Erro", message="No Data File Found!")
    else:
        if website in data.keys():
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email: {email}\npassword: {password}")
        else:
            messagebox.showinfo(title="Erro", message=f"No Details Of {website} Exists!")





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#image canvas
canvas = Canvas(width=200, height=200)
lock_imp = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_imp)
canvas.grid(column=1, row=0)

# label 'Website:'
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# label 'Email/Username:'
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

# label 'Password:'
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# website_entry
website_entry = Entry(width=25)
website_entry.focus()
website_entry.grid(column=1, row=1)

# username_entry
username_entry = Entry(width=40)
username_entry.insert(0, 'lucky@gmail.com')
username_entry.grid(column=1, row=2, columnspan=2)

# password_entry
password_entry = Entry(width=25)
password_entry.grid(column=1, row=3)

# Buttons
# generate password button:
generate_password = Button(text='Generate Password', command=gen_password)
generate_password.grid(column=2, row=3)

# add button:
add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

# search button:
search_button = Button(text="Search", fg="blue", width=15, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()

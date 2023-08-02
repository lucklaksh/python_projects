from tkinter import *
from tkinter import messagebox
import random
import pyperclip
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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        is_ok = False
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\nEmail:{email}\nPassword:{password}\nIs it OK to Save?")

    if is_ok:
        with open("data.txt", mode='a') as data:
            data.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


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
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

# username_entry
username_entry = Entry(width=40)
username_entry.insert(0, 'lucky@gmail.com')
username_entry.grid(column=1, row=2, columnspan=2)

# password_entry
password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

# Buttons
# generate password button:
generate_password = Button(text='Generate Password', command=gen_password)
generate_password.grid(column=2, row=3)

# add button:
add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

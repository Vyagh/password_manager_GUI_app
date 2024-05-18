from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="You left some Fields Empty")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"Your Details are:\nEmail/Username:{email_username}\n"
                                                                f"Password:{password}\nDo you want to Save it?")
        if is_okay:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website}|{email_username}|{password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)


canvas = Canvas(width=155, height=170)
logo = PhotoImage(file="logo.png")
canvas.create_image(60, 90, image=logo)
canvas.grid(column=1, row=0)


# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_username_entry = Entry(width=35)
email_username_entry.insert(0, "Vyagh.vy@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3)

# Buttons
add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)

generate_password_button = Button(text="Generate", command=generate)
generate_password_button.grid(column=2, row=3)















window.mainloop()







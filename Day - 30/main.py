# Importing tkinter module
from tkinter import *
# Import message box from tkinter
from tkinter import messagebox
# Importing random module package
from random import choice, randint, shuffle
# Importing pyperclip
import pyperclip
# Importing json module
import json

# Create a function to find password
def find_password():
    # Get a website entry
    website = website_entry.get()
    # try the implementation
    try:
        # Make a json file to save info
        with open("data.json", "r") as data_file:
            # Load the json data
            data = json.load(data_file)
            # format the search email
            search_email = data[website]['email']
            # format the search password
            search_password = data[website]['password']
            # show the messagebox
            messagebox.showinfo(title=website.title(), message=f"Email: {search_email}\nPassword: {search_password}")
    # Except the error
    except FileNotFoundError:
        # Show the error in messagebox
        messagebox.showerror(title="Error", message="No Data File Found")
    # Except the error
    except KeyError:
        # Show the error in messagebox
        messagebox.showerror(title="Error", message="No details for the website exists")

# Define a function to generate password
def generate_password():
    # Get a list of alphabets
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # get a list of numbers
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Get a list of symbols
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # using for loop hold the letters, symbols and numbers
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # add all the hold variables in password list
    password_list = password_letters + password_symbols + password_numbers
    # shuffle the password list
    shuffle(password_list)

    # Join the password list
    password = "".join(password_list)
    password_entry.insert(0, password)
    # Copy the generate password to clipboard
    pyperclip.copy(password)

# Def a function to clear the info
def clear_info():
    # delete the website entry
    website_entry.delete(0, END)
    # delete the password entry
    password_entry.delete(0, END)

# Define a function to save info
def save():
    # Assign all the entry into variables
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # Show the boilerplate of formated data
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # Making conditions
    if len(website) == 0 or len(password) == 0:
        # show the messagebox
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        # Try condition
        try:
            with open("data.json", "r") as data_file:
                # Load the json data
                data = json.load(data_file)
        # Except the error
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry()
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry()
email_entry.grid(row=2, column=1)
email_entry.insert(0, "phillip@email.com")
password_entry = Entry()
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Save Info", command=save)
add_button.grid(row=6, column=1)
search_button = Button(text="Search Website", command=find_password)
search_button.grid(row=1, column=2)
clear_button = Button(text="Clear Info", command=clear_info)
clear_button.grid(row=2, column=2)


window.mainloop()

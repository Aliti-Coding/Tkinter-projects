from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
FONT_NAME = "Courier"
Light_yellow = "#FFFFD0"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():        
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8,10))]
    number = [password_list.append(choice(numbers)) for char in range(randint(2,4))]
    symbol = [password_list.append(choice(symbols)) for char in range(randint(2,4))]

    shuffle(password_list)
    return ''.join(password_list)

def password_gen_button():
    password = password_gen()
    print(password)
    entry_password.insert(END, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    webiste_text = entry_website.get()
    email_username_text = entry_email_username.get()
    password_text = entry_password.get()

    new_data = {
        webiste_text: {
            "email": email_username_text,
            "password": password_text
        }
    }

    if len(webiste_text) < 1 or len(password_text) < 1:
        messagebox.showwarning(title="Warning", message="There are empty text entries, \nplease fill them up!")
    else:
        try:
            with open("data.json", "r") as datafile:
                data = json.load(datafile)
                data.update(new_data)
        except FileNotFoundError:    
            with open("data.json", "w") as datafile:
                json.dump(new_data, datafile, indent=4)
        else:
            with open("data.json", "w") as datafile:
                json.dump(data, datafile, indent=4)
        finally:
                entry_website.delete(0, END)
                entry_password.delete(0, END)
                entry_website.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=r"password_manager\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#buttons
button_gen_pass = Button(text="Generate Password",font=(FONT_NAME, 10), bg=Light_yellow, command=password_gen_button)
button_gen_pass.grid(column=2, row=3)

button_add = Button(text="Add",font=(FONT_NAME, 10), bg=Light_yellow, width=49, command=add_to_file)
button_add.grid(column=1, row=4, columnspan=2)


#Entry boxes
entry_website = Entry(width=65)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()

entry_email_username = Entry(width=65)
entry_email_username.insert(END, "fehmmialiti@gmail.com")
entry_email_username.grid(column=1, row=2, columnspan=2)

entry_password = Entry(width=41)
entry_password.grid(column=1, row=3)



#Labels
label_website = Label(text="Website: ", font=(FONT_NAME, 10))
label_website.grid(column=0, row=1)

label_email_username = Label(text="Email/Username: ", font=(FONT_NAME, 10))
label_email_username.grid(column=0, row=2)

label_Password = Label(text="Password: ", font=(FONT_NAME, 10))
label_Password.grid(column=0, row=3)



window.mainloop()
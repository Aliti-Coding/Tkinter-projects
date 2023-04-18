#UNFINISHED PROJECT

from tkinter import *
import random
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"

df = pd.read_csv(r"flash_card_app\data\french_words.csv")
to_learn = df.to_dict(orient="records")


window = Tk()
window.title("Flash card app")
window.config(padx=50, pady=100,bg=BACKGROUND_COLOR)


# ---------------------------- UI SETUP ------------------------------- #
#images
right_img = PhotoImage(file=r"flash_card_app\images\right.png")
wrong_img = PhotoImage(file=r"flash_card_app\images\wrong.png")
card_back_img = PhotoImage(file=r"flash_card_app\images\card_back.png")
card_front_img = PhotoImage(file=r"flash_card_app\images\card_front.png")

#canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image(400, 266, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

#Labels
label_languange = Label(text="", font=("arial", 40, "italic"))
label_languange.place(x=320, y=130)

label_word = Label(text="", font=("arial", 60, "bold"))
label_word.grid(column=0, row=0, columnspan=2)
# ---------------------------- Vocabulary ------------------------------- #
def flipcard():
    canvas.itemconfig(canvas_img, image=card_back_img)
    random_word = random.choice(to_learn)
    english_word = random_word['English']
    label_word.config(text=english_word, fill="white", fg="white")
    label_languange.config(text="English", bg=BACKGROUND_COLOR)


def words():
    random_word = random.choice(to_learn)
    french_word = random_word['French']
    label_word.config(text=french_word)
    label_languange.config(text="French")


    print(french_word)
print(words())

window.after(3000, func=flipcard)
window.after_cancel(window)

#buttons
button_wrong = Button(image=wrong_img, highlightthickness=0, command=words)
button_wrong.grid(column=0,row=2)

button_right = Button(image=right_img, highlightthickness=0, command=words)
button_right.grid(column=1, row=2)

words()

window.mainloop()

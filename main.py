from tkinter import *
import random
import pandas as pd

# ---------------------------- CONSTANTS ------------------------------- #

words_shown = []

# ---------------------------- READ THE CSV FILE ------------------------------- #

try:
    data = pd.read_csv("data/words_to_learn.csv")
except:
    data = pd.read_csv("data/french_words.csv")
words = data.to_dict(orient="records")

# ---------------------------- FUNCTIONS ------------------------------- #


def next_word(*args):
    word = random.choice(words)
    words_shown.append(word)
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(card_word, text=word['French'], fill='black')
    canvas.itemconfig(card_title, text='French', fill='black')
    window.after(3000, show_word, word)
    if args and len(words_shown) > 1:
        if words_shown[-2] in words:
            words.remove(words_shown[-2])

        updated_words = pd.DataFrame(words)

        updated_words.to_csv('data/words_to_learn.csv', index=False)


def show_word(word):
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(card_word, text=word['English'], fill='white')
    canvas.itemconfig(card_title, text='English', fill='white')

# ---------------------------- UI SETUP ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=card_front)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=wrong_image, highlightthickness=0, command=next_word)
cross_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
check_button = Button(image=right_image, highlightthickness=0, command=lambda: next_word(1))
check_button.grid(row=1, column=1)

next_word()

window.mainloop()

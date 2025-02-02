from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer) # cancels the timer until we set up the new card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card) # only flips after waiting on a card for 3 seconds


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card) # removes the dictionary from the list "to_learn"
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
tick_img = PhotoImage(file="images/right.png")
cross_img = PhotoImage(file="images/wrong.png")

# canvas (the flashcard)
canvas = Canvas(width=800, height=526, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

# buttons
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card)  # highlight thickness manages the border
unknown_button.grid(column=0, row=1)
known_button = Button(image=tick_img, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
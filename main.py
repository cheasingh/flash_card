from tkinter import Tk, Button, Entry, Label, Canvas, PhotoImage
import pandas
from random import choice
import json

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("./data/french_words.csv")
# test = data[data.French == "mois"].English
# print(str(test.values[0]))

# print(choice(data.French))

# -----------------------------Function----------------------------


def gen_word():
    canvas.itemconfig(answer_text, text=f"{choice(data.French)}")


def translate(language, text):
    language = language.title()

    if language == "English":
        word = data[data.French == text].English
    else:
        word = data[data.English == text].French

    return word.values[0]


def flip_card(front):

    if front == True:
        canvas.itemconfig(language_text, text="English")
        canvas.itemconfig(card, image=img_back)

        french = canvas.itemcget(answer_text, "text")
        canvas.itemconfig(answer_text, text=translate("English", french))

    else:
        canvas.itemconfig(card, image=img_front)
        canvas.itemconfig(language_text, text="French")
        gen_word()

    window.after(3000, flip_card, not front)


    # -----------------------------UI Design---------------------------
window = Tk()
window.title("App Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# canvas estate

canvas = Canvas(width=800, height=525,
                bg=BACKGROUND_COLOR, highlightthickness=0)
img_front = PhotoImage(file="./images/card_front.png")
img_back = PhotoImage(file=f"./images/card_back.png")


card = canvas.create_image(400, 265, image=img_front)

language_text = canvas.create_text(
    400, 150, text="French", fill="black", font=("Arial", 40, "italic"))

answer_text = canvas.create_text(
    400, 263, text="trouve", fill="black", font=("Arial", 60, "italic"))


flip_card(False)


canvas.grid(row=0, column=0, columnspan=2)


# button estate
# right button
img_right = PhotoImage(file="./images/right.png")
btn_right = Button(image=img_right, width=80, height=80,
                   highlightthickness=0, command=gen_word)
btn_right.grid(row=1, column=0)

# wrong button
img_wrong = PhotoImage(file="./images/wrong.png")
btn_wrong = Button(image=img_wrong, width=80, height=80,
                   highlightthickness=0, command=gen_word)
btn_wrong.grid(row=1, column=1)


window.mainloop()

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    file = pandas.read_csv("data/new_eng_russ.csv")
except:
    data = pandas.read_csv("data/english_russian.csv")
    ss = data.to_dict(orient="records")
else:
    ss = file.to_dict(orient="records")



word_random = {}
#__________________WORD Translate__________________#
def learnd_word():
    global ss
    ss.remove(word_random)
    learning = pandas.DataFrame(ss)
    learning.to_csv("data/new_eng_russ.csv", index=False)
    random_word()


#__________________WORD Translate__________________#
def word_translate():
    front_card.itemconfig(front, image=card_back)
    front_card.itemconfig(lang, text="Russian", fill="white")
    front_card.itemconfig(new, text=word_random["Russian"], fill="white")

#__________________WORD FLASH__________________#
def random_word():
    global word_random, flip_timer
    window.after_cancel(flip_timer)
    word_random = random.choice(ss)
    front_card.itemconfig(front, image=card_front)
    front_card.itemconfig(lang, text="English", fill="black")
    front_card.itemconfig(new, text=word_random["English"], fill="black")
    flip_timer = window.after(3000, func=word_translate)



window = Tk()
window.config(width=800, height=800, padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)
window.title("Language Learning Cards")
flip_timer = window.after(3000, func=word_translate)

#Images
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

#Front Card
front_card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front = front_card.create_image(400, 263, image=card_front)
lang = front_card.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
new = front_card.create_text(400, 283, text="trouve", font=("Ariel", 60, "bold"))
front_card.grid(row=0, column=0 , columnspan=2)

#Button
wrong_butoon = Button(image=wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=random_word)
wrong_butoon.grid(row=1, column=0)

right_butoon = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR, command=learnd_word)
right_butoon.grid(row=1, column=1)

random_word()






window.mainloop()
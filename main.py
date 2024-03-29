BACKGROUND_COLOR = "#B1DDC6"
import pandas
from tkinter import *
import random
to_learn={}
current_card = {}
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn=original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')



def flip_card():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=front_img)
    current_card = random.choice(to_learn)
    french = current_card['French']

    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=french, fill='black')
    flip_timer = window.after(3000, func=flip_card)
def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv',index=False)
    next_card()



window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
back_img = PhotoImage(file='images/card_back.png')
front_img = PhotoImage(file='images/card_front.png')
canvas_image = canvas.create_image(400, 263, image=front_img)

card_title = canvas.create_text(400, 150, text='Title', fill='black', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='English', fill='black', font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_button_image = PhotoImage(file='images/right.png')
wrong_button_image = PhotoImage(file='images/wrong.png')

right_button = Button(image=right_button_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
wrong_button = Button(image=wrong_button_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)

right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)
next_card()

window.mainloop()

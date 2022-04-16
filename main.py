from tkinter import * 
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}

# Loading file 

try:
    data = pd.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else: 
    to_learn = to_learn = data.to_dict(orient="records")



current_card = {}


def next_card():
    """
    This will display the next word from the word dict 
    """
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French", fill="black")
    canvas.itemconfig(card_word, text = current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    timer = window.after(3000, func=flip_card)

def flip_card():
    """
    This Function will flip the card and show the meaning of the word
    """
    canvas.itemconfig(card_title, text = "English", fill="white")
    canvas.itemconfig(card_word, text = current_card["English"], fill="white")
    canvas.itemconfig(card_background, image = card_back )

def is_known():
    """
    This function will remove the word from the list 
    of the word
    """
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()





# GUI 
# Window
window =Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Changing the meaning
timer = window.after(3000, func=flip_card)


# Canvas
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

# Camvas text
card_title = canvas.create_text(400, 150, text="",font=("Ariel", 40, "italic"))

card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))



# buttons
wrong_img = PhotoImage(file="images\wrong.png")
unknown_button = Button(image=wrong_img,highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

correct_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0, command=is_known)
correct_button.grid(row=1, column=1)




next_card()
window.mainloop()
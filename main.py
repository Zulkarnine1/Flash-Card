BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"

# Imports
from tkinter import *
import pandas as pd
import random

# ================  Get The Data  ================
try:
    data = pd.read_csv("data/words_to_learn.csv")
except:
    data = pd.read_csv("data/chinese_chars.csv")

data = data.to_dict(orient="records")
print(len(data))
picked = {}

def pick_word1():
    global picked,flip_timer
    window.after_cancel(flip_timer)
    if picked!={}:
        data.remove(picked)
    picked = random.choice(data)
    canvas.itemconfig(text1,text=picked["Chinese"], fill="black")
    canvas.itemconfig(text2,text=picked["Pinyin"], fill="black")
    canvas.itemconfig(card_title, text="Chinese", fill="black")
    canvas.itemconfig(card, image=image_data)
    flip_timer = window.after(3000,func=flip_card)


def pick_word2():
    global picked, flip_timer
    window.after_cancel(flip_timer)
    picked = random.choice(data)
    canvas.itemconfig(text1, text=picked["Chinese"], fill="black")
    canvas.itemconfig(text2, text=picked["Pinyin"], fill="black")
    canvas.itemconfig(card_title, text="Chinese", fill="black")
    canvas.itemconfig(card, image=image_data)
    flip_timer = window.after(3000, func=flip_card)


# ================  Timer  ================

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(text1, text=picked["English"],fill="white")
    canvas.itemconfig(text2, text="")
    canvas.itemconfig(card, image=image_data1)


# ================  Setting up UI  ================
window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
image_data= PhotoImage(file="images/card_front.png")
image_data1= PhotoImage(file="images/card_back.png")
card = canvas.create_image(400,263,image=image_data)
card_title = canvas.create_text(400,150,text="Chinese",font=(FONT,40,"italic"))
text1 = canvas.create_text(400,263,text="",font=(FONT,60,"bold"))
text2 = canvas.create_text(400,343,text="",font=(FONT,30,"normal"))
canvas.grid(column=0,row=0,columnspan=2)


img1 = PhotoImage(file="images/right.png")
button1 = Button(image=img1, highlightthickness=0,command=pick_word1)
button1.grid(row=1,column=1)

img2 = PhotoImage(file="images/wrong.png")
button2 = Button(image=img2, highlightthickness=0,command=pick_word2)
button2.grid(row=1,column=0)

pick_word1()


window.mainloop()

end_dict = {
    "English":[],
    "Pinyin":[],
    "Chinese":[],
}
for item in data:
    end_dict["English"].append(item["English"])
    end_dict["Pinyin"].append(item["Pinyin"])
    end_dict["Chinese"].append(item["Chinese"])
df = pd.DataFrame(end_dict)
df.to_csv("./data/words_to_learn.csv")
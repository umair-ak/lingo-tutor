from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

# ------------- reading from csv file and displaying on the card----------------

data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient='records')


def change_word():
    new_word = random.choice(data_dict)
    changing_text = new_word['French']
    canva.itemconfig(word,text = changing_text)

# --------------------------------- fliping card --------------------------------
# ---------------------------------  --------------------------------
# --------------------------------- UI --------------------------------
screen = Tk()
screen.title('Lingo Tutor')
screen.minsize(width=900,height=800)
screen.config(background=BACKGROUND_COLOR,padx=50,pady=50)

# canva stuff
canva = Canvas(height=580,width=800,bg= BACKGROUND_COLOR,highlightthickness=0)
card = PhotoImage(file='images/card_back.png')
canva.create_image(400,300,image = card)

title = canva.create_text(400,150,text='French',font = ('ariel',30,'italic'))
word = canva.create_text(400,300,text='WORD',font = ('ariel',40,'bold')) 

canva.grid(row=1,column=1,columnspan=2)

# image buttons 
right_img = PhotoImage(file='images/right.png')
right = Button(image=right_img , highlightthickness=0 , command=change_word)

wrong_img = PhotoImage(file='images/wrong.png')
wrong = Button(image=wrong_img,command= change_word)

wrong.grid(row=2,column=1)
right.grid(row=2,column=2)

change_word()
screen.mainloop()
from cgitb import text
from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
data_dict = {}
# ------------- reading from csv file and displaying on the card----------------
try :
    data = pandas.read_csv("data/stillunknownwords.csv")

except FileNotFoundError:
    data = pandas.read_csv("data/French_words.csv")
    data_dict = data.to_dict(orient='records')
except pandas.errors.EmptyDataError:
    data = pandas.read_csv("data/French_words.csv")
    data_dict = data.to_dict(orient='records')

else:
    data_dict = data.to_dict(orient='records')

new_word = {}
def change_word():
    global new_word,timer,data_dict
    screen.after_cancel(timer)
    try :
        new_word = random.choice(data_dict)
    
    except IndexError:
        ennd()
        
    else:
        changing_text = new_word['French']
        canva.itemconfig(word,text = changing_text,fill = 'white')
        canva.itemconfig(title,text = "French",fill = 'white')
        canva.itemconfig(front,image = front_card)
    timer = screen.after(3000,func=flip)    


# --------------------------------- fliping card --------------------------------
def flip():
    canva.itemconfig(front,image = back_card)
    canva.itemconfig(word,text = new_word['English'],fill = 'black')
    canva.itemconfig(title,text = "English",fill = 'black')
    
    
# -----------------------------------saving the details--------------------------
def ennd():
    screen.after_cancel(timer)
    canva.itemconfig(word,text="You have learned 100 words")
    canva.itemconfig(title,text="Congrats !")
    pass
def is_known():
    global new_word
    try :
        data_dict.remove(new_word)
    except ValueError:
        ennd()
    changedict = pandas.DataFrame(data_dict)
    changedict.to_csv('data/stillunknownwords.csv' , index=False)
    change_word()
# --------------------------------- UI --------------------------------
screen = Tk()
screen.title('Lingo Tutor')
screen.minsize(width=900,height=800)
screen.config(background=BACKGROUND_COLOR,padx=50,pady=50)

# canva stuff
canva = Canvas(height=580,width=800,bg= BACKGROUND_COLOR,highlightthickness=0)
front_card = PhotoImage(file='images/card_back.png')
back_card = PhotoImage(file='images/card_front.png')
front = canva.create_image(400,300,image = front_card)

title = canva.create_text(400,150,text='French',font = ('ariel',30,'italic'),fill='white')
word = canva.create_text(400,300,text='WORD',font = ('ariel',40,'bold')) 

canva.grid(row=1,column=1,columnspan=2)

# image buttons 
right_img = PhotoImage(file='images/right.png')
right = Button(image=right_img , highlightthickness=0 , command=is_known)

wrong_img = PhotoImage(file='images/wrong.png')
wrong = Button(image=wrong_img,command= change_word)

wrong.grid(row=2,column=1)
right.grid(row=2,column=2)

timer = screen.after(3000,func=flip)

change_word()
screen.mainloop()
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------------  --------------------------------
# ---------------------------------  --------------------------------
# ---------------------------------  --------------------------------
# --------------------------------- UI --------------------------------
screen = Tk()
screen.title('Lingo Tutor')
screen.minsize(width=900,height=800)
screen.config(background=BACKGROUND_COLOR,padx=50,pady=50)
canva = Canvas(height=580,width=800,bg= BACKGROUND_COLOR,highlightthickness=0)
card = PhotoImage(file='images/card_back.png')
canva.create_image(400,300,image = card)
canva.grid(row=1,column=1,columnspan=2)
back_label_eng = Label(text='English',font = ('ariel',40,'italic'))
# back_label_eng = Label(text='',font = ('ariel',40,'itallic'))
right_img = PhotoImage(file='images/right.png')
right = Button(image=right_img , highlightthickness=0)
right.grid(row=2,column=2)

wrong_img = PhotoImage(file='images/wrong.png')
wrong = Button(image=wrong_img)
wrong.grid(row=2,column=1)
screen.mainloop()
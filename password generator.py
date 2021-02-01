from tkinter import *
import string,random


itc=Tk()
itc.geometry("500x380")
itc.title("ITC PASSWORD GENERATOR")
Label(text="ITC PASSWORD GENERATOR", bg="black", width="100").pack()

title = StringVar()
label = Label(itc, textvariable=title).pack()
title.set("Password Type:")

def project():
    selection=choice.get()

choice=IntVar()
CS1=Radiobutton(itc,text="NORMAL",variable=choice,value=1,command=project).pack(anchor=CENTER)
CS2=Radiobutton(itc,text="STRONG",variable=choice,value=2,command=project).pack(anchor=CENTER)
CS3=Radiobutton(itc,text="ADVANCED",variable=choice,value=3,command=project).pack(anchor=CENTER)
CS4=Radiobutton(itc,text="DIGIT",variable=choice,value=4,command=project).pack(anchor=CENTER)


labelchoice=Label(itc)
labelchoice.pack()
lenlabel=StringVar()
lenlabel.set("PASSWORD TYPE:")


lentitle=Label(itc, textvariable=lenlabel).pack()

val=IntVar()
passlen = Spinbox(itc, from_=1, to_=100, textvariable=val, width=13).pack()


def callback():
    lsum.config(text=passgen())

passgenButton=Button(itc, text="Generate Password",bd=4,height=1,command=callback, pady=3)
passgenButton.pack()
password=str(callback)



lsum=Label(itc,text="")
lsum.pack(side=BOTTOM)

normal=string.ascii_uppercase+string.ascii_lowercase
strong=string.ascii_uppercase+string.ascii_lowercase+string.digits
advanced=normal+strong+string.punctuation
digit=string.digits

def passgen():
    if choice.get()==1:
        return "".join(random.sample(normal,val.get()))
    elif choice.get()==2:
        return "".join(random.sample(strong,val.get()))  
    elif choice.get()==3:
        return "".join(random.sample(advanced,val.get()))
    elif choice.get()==4:
        return "".join(random.sample(digit,val.get()))

itc.mainloop()
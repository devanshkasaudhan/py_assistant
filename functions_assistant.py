from tkinter import *



root = Tk()

e = Entry(root, width=50, bg="black", fg="white",borderwidth=5)
e.pack()

def myClick():
    myLable = Label(root,text="hello, "+ e.get())
    myLable.pack()

myButton = Button(root, text="enter your name ", command=myClick)
myButton.pack()

root.mainloop()
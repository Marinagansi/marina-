from tkinter import*
root=Tk()
def show():
    mylabel=Label(root,text=clicked.get()).pack()


options=[
    "moday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
]
clicked=StringVar()
clicked.set("week")
drop=OptionMenu(root,clicked, *options)
drop.pack()
myButton=Button(root,text="show selection",command=show).pack()
mainloop()
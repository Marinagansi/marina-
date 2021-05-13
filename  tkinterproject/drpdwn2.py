from tkinter import*
root=Tk()
def show():
    my_label=Label(root, text=clicked.get()).pack()
clicked=StringVar()
clicked.set("week")
drop=OptionMenu(root, clicked,"monday","tuesday","wednesday","thursday")
drop.pack()
mybutton=Button(root, text="show selection", command=show).pack()
mainloop()
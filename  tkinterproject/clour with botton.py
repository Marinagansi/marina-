from tkinter import*
root=Tk()
def myclick():
    mylabel=Label(root, text="oline class")
    mylabel.pack()
mybutton=Button(root, text="hello everyone",  command=myclick, fg="red", bg="blue")
mybutton.pack()
root.mainloop()
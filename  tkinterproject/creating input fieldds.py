from tkinter import*
root=Tk()
e1=Entry(root,width=50,fg="blue", bg="green", borderwidth=5)
e1.pack()
def myclick():
    textoutput="hello" + e1.get()
    mylabel=Label(root,text=textoutput).pack()
mybutton=Button(root,text="click me", command=myclick).pack()
root.mainloop()


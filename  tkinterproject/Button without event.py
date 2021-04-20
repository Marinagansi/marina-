from tkinter import*
root=Tk()
def myclick():
    mylabel=Label(root,text="button is clicked")
    mylabel.pack()
mybutton=Button(root,text="click me!", command =myclick).pack()
root.mainloop()
from tkinter import*
root=Tk()
root.title("check box")
def show():
    mylabel= Label(root,text=var.get()).pack()
var=StringVar()
checkButton=Checkbutton(root, text="agree",
                        variable=var, onvalue="on", offvalue="off")
checkButton.deselect()
checkButton.pack()

myButton=Button(root,text="show",command=show).pack()
mainloop()
from tkinter import*
root=Tk()
MODES=[
    ("female","f"),
    ("male","m"),
    ("third gender","t")
]
gender = StringVar()
gender.set("f")
for text, mode in MODES:
     Radiobutton(root,text=text, variable=gender, value=mode).pack(anchor=W)
def click(value):
    mylabel=Label(root,text=value)
    mylabel.pack()
myButton=Button(root,text="click",command=lambda :click(gender.get())).pack()
mainloop()
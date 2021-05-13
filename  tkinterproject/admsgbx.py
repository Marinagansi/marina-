from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("message box")
root.iconbitmap("emoji.ico")
def popup():
    messagebox.showinfo("this is my Popup","hello world")
Button(root,text="Popup",command=popup).pack()
mainloop()
from tkinter import*
root=Tk()
def open():
    global my_img
    top=Toplevel()
    top.title("check new window")
    my_label= Label(top,text="h").pack()
    btn2=Button(top, text="close window", command= top.destroy).pack()
btn=Button(root,text="open",command=open).pack()
mainloop()
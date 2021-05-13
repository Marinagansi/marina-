from tkinter import*
root=Tk()
root.title("slider")

vertical=Scale(root,from_=0,to=200)
vertical.pack()
#horizontal
horizontal=Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal .pack()
my_label=Label(root, text=horizontal.get()).pack()
def slide():
    my_label=Label(root,text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

my_btn=Button(root, text="click me",command=slide).pack()
mainloop()
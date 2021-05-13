from tkinter import*
from PIL import ImageTk,Image
from tkinter import filedialog
root=Tk()
root.title("dialog box")
def open():
    global my_img
    root.filename=filedialog.askopenfilename(initialdir="/desktop",title="facebook",
                                             filetypes=(("png files", "*.png"),("all files","*.*")))
    my_label=Label(root, text=root.filename).pack()
    my_image=ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label=Label(image=my_image).pack()
btn=Button (root,text="open file",command=open).pack()
mainloop()
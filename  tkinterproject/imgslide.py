from tkinter import*
from PIL import ImageTk
Image
root=Tk()
root.tittle("picture slide")
my_img1=ImageTk.PhotoImage(Image.open('insta.png'))
my_img2=ImageTk.PhotoImage(Image.open('facebook.png'))
my_img3=ImageTk.PhotoImage(Image.open('whatsapp.png'))
image_list=[my_img1,my_img2,my_img_3]

my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,colummspan=3)
def forward(image_number):
     global my_label
     global button_forward
     global button_back
     my_label.grid_forget()
     my_label=Label(image=image_list[image_number]
     button_forward=Button(root,text='>>,command=lambda:forward(image_number+1)
     button_back=Button(root,text='<<', command=lambda:forward(image_number-1)
         if image_number==3:
            button_forward =Button(root,text ='>>', state=DISABLED)
            my_label.grid(row=0,column=0,columnspan=3)
            buton_back.grid(row=1,column=0)
            buton_forward.grid(row=1, column=2)


def back(image_number):
    global my_label
    global button_forward
    global button_back
    global button_exit
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number]
    button_forward = Button(root,text = '>>', command = lambda: forward(image_number + 1)
    button_back = Button(root,text = '<<', command = lambda: forward(image_number - 1)
    if image_number == 1:
        button_back = Button(root,text = '<<', state = DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    buton_back.grid(row=1, column=2)
    buton_forward.grid(row=1, column=2)


    button_back=Button(root,text='>>', command=lambda:forward(2))
    button_exit=Button(root,text="exit",command=root.quit)
    buton_back.grid(row=1, column=0)
    buttoln_exit,grid(row=1,column=1)
    buton_forward.grid(row=1, column=2)


mainloop()

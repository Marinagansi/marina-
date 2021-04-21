from tkinter import*
cal=Tk()
 #defining the title
cal.title("calculator")
cal.iconbitmap("calimage.ico")

e=Entry(cal,width=40, bg="light blue",borderwidt=15)
e.grid(row=0,  column=0,columnspan=4, padx=10,  pady=10)

def button_click(number):
    current=e.get ()
    e.delete(0,END)
    e.insert(0,str(current) +str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number=e.get()
    global f_num
    global operation
    operation="add"
    f_num=int(first_number)
    e.delete(0,END)
def button_sub():
    first_number=e.get()
    global f_num
    global operation
    operation = "sub"
    f_num=int(first_number)
    e.delete(0,END)



def button_multi():
    first_number=e.get()
    global f_num
    global operation
    operation="multi"
    f_num=int(first_number)
    e.delete(0,END)

def button_div():
    first_number=e.get()
    global f_num
    global operation
    operation="div"
    f_num=int(first_number)
    e.delete(0,END)


def button_equal():
    second_number=e.get()
    e.delete(0, END)
    if operation=="add":
        e.insert(0, f_num + int(second_number))
    if operation=="sub":
        e.insert(0, f_num - int(second_number))
    if operation=="multi":
        e.insert(0, f_num * int(second_number))
    if operation=="div":
        e.insert(0,f_num / int(second_number))


button_1=Button(cal, text="1",padx=39,pady=20,fg="white", bg="black",command=lambda:button_click(1))
button_2=Button(cal, text="2",padx=39,pady=20,fg="white", bg="black", command=lambda:button_click(2))
button_3=Button(cal, text="3",padx=39,pady=20, fg="white", bg="black",command=lambda:button_click(3))
button_4=Button(cal, text="4",padx=39,pady=20, fg="white", bg="black",command=lambda:button_click(4))
button_5=Button(cal, text="5",padx=39,pady=20,fg="white", bg="black",command=lambda:button_click(5))
button_6=Button(cal, text="6",padx=39,pady=20,fg="white", bg="black", command=lambda:button_click(6))
button_7=Button(cal, text="7",padx=39,pady=20,fg="white", bg="black", command=lambda:button_click(7))
button_8=Button(cal, text="8",padx=39,pady=20,fg="white", bg="black", command=lambda:button_click(8))
button_9=Button(cal, text="9",padx=39,pady=20,fg="white", bg="black", command=lambda:button_click(9))
button_0=Button(cal, text="0",padx=39,pady=20,fg="white", bg="black", command=lambda:button_click(0))
button_add=Button(cal, text="+",padx=39,pady=20,fg="white",bg="black", command=button_add)
button_equal=Button(cal, text="=",padx=39,pady=20, fg="black", bg="bisque3",command=button_equal)
button_clear=Button(cal, text="clear",padx=110,pady=20,fg="black", bg="bisque3", command=button_clear)
button_sub= Button(cal, text="-", padx=39, pady=20,fg="white",bg="black", command=button_sub)
button_multi=Button(cal, text="*",padx=39,pady=20,fg="white",bg="black", command=button_multi)
button_div=Button(cal,text="/",padx=40,pady=20,fg="white",bg="black",command=button_div)

button_1.grid(row=1,column=0)
button_2.grid(row=2,column=0)
button_3.grid(row=3,column=0)

button_4.grid(row=1,column=1)
button_5.grid(row=2,column=1)
button_6.grid(row=3,column=1)

button_7.grid(row=1,column=2)
button_8.grid(row=2,column=2)
button_9.grid(row=3,column=2)

button_0.grid(row=4,column=0)
button_sub.grid(row=4,column=2)
button_multi.grid (row=5,column=2)
button_add.grid(row=4, column=1)
button_div.grid(row=5,column=0)
button_equal.grid(row=5, column=1)
button_clear.grid(row=6,column=0,columnspan=3)
cal.mainloop()

from tkinter import*
root = Tk()
root.geometry("500x300")
root.title("python")
def getvals():
    print("accepted")
Label(root, text="python registration form", font="arial 15 bold").grid(row=0,column=3)
# creating Labels
name = Label(root, text="name")
phone = Label(root, text="phone")
address = Label(root, text="address")
emergency = Label(root, text="emergency")
paymentmood = Label(root, text="paymentmethod")
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
address.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmood.grid(row=5,column=2)

#creating varaiable to store value
namevalue=StringVar
phonevalue=StringVar
addressvalue=StringVar
emergencyvalue = StringVar
paymentmoodvalue = StringVar
checkvalue=IntVar

#creating entry field
tname = Entry(root,textvariable=namevalue)
tname.grid(row=1,column=3)
tphone = Entry(root,textvariable=phonevalue)
tphone.grid(row=2,column=3)
taddress=Entry(root,textvariable=addressvalue)
taddress.grid(row=3,column=3)
temergency= Entry(root,textvariable=emergencyvalue)
temergency.grid(row=4,column=3)
tpaymentmood= Entry(root,textvariable=paymentmoodvalue)
tpaymentmood.grid(row=5,column=3)

#creating checkbutton
checkbtn=Checkbutton(text="remember me?",variable=checkvalue)
checkbtn.grid(row=6,column=3)

#submit button
Button(text="submit",command=getvals).grid(row=7,column=3)

root.mainloop()
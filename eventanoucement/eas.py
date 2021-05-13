from tkinter import*
from tkinter import ttk

class event():
    def __init__(self,root):
         self.root=root
         self.root.title("event management system")
         self.root.geometry("1370x700+0+0")
         title=Label(root,text="event management system",bd=6,relief=GROOVE, font=("times new roman",50,"bold"),bg="blUe", fg="yellow")
         title.pack(side=TOP,fill=X)
         frame=Frame(self.root, bd=9,relief=RIDGE,padx=20,bg="powder blue").place(x=10,y=100,width=1350, height=400)
         #=======dataframeleft=====
         Dataframeleft=LabelFrame(frame,text="participation", bd=6,  bg="powder blue", fg="green", font=("times new roman",10,"bold"))
         Dataframeleft.place(x=30,y=130,width=700,height=350)

         # =====creating combobox========
         lblmember=Label(Dataframeleft, text="Member",bg="powder blue",font=("arial",15)).grid(row=0,column=0,sticky=W)
         comember=ttk.Combobox(Dataframeleft,font=("arial",10),width=26,state="readonly")
         comember["value"]=("admin staff", "staff","student","lectural")
         comember.grid(row=0,column=1,sticky=W)
#====creating text column=====
         lbladdress=Label(Dataframeleft, bg="powder blue"  ,text="Address",font=("arial",15),padx=2,pady=3).grid(row=1,column=0)
         textaddress=Entry(Dataframeleft,font=("arial",10),width=28).grid(row=1,column=1,sticky=W)

         lblcontact=Label(Dataframeleft, bg="powder blue"  ,text="Phone no",font=("arial",15),padx=2,pady=3).grid(row=2,column=0)
         textcontact=Entry(Dataframeleft,font=("arial",10),width=28).grid(row=2,column=1,sticky=W)

         lblemail = Label(Dataframeleft, bg="powder blue", text="Email", font=("arial", 15), padx=2, pady=3).grid(
             row=3, column=0)
         textemain= Entry(Dataframeleft, font=("arial", 10), width=28).grid(row=3, column=1, sticky=W)

         # ====creating COMBOBOX=====
         lblgender=Label(Dataframeleft, text="gender", bg="powder blue",font=("arial",15)).grid(row=4,column=0,sticky=W)
         cogender = ttk.Combobox(Dataframeleft, font=("arial", 10), width=26, state="readonly")
         cogender["value"] = ("female", "male", "other")
         cogender.grid(row=4, column=1, sticky=W)


#=====dATA FRAME RIGHT===
         Dataframeright=LabelFrame(frame,text="EVENTS",bd=6,bg="powder blue",fg="green",font=("times new romen",10, "bold"))
         Dataframeright.place(x=750,y=130,width=590,height=350)

#======button frame
         buttonframe=LabelFrame(frame,bd=6,bg="powder blue")
         buttonframe.place(x=10,y=505,width=1350,height=60)
#====information frame=====
         infoframe=LabelFrame(frame,bd=6,bg="powder blue").place(x=10,y=570,width=1350,height=120)


class event():
    pass
    root=Tk()
    obj=event(root)
    root.mainloop()
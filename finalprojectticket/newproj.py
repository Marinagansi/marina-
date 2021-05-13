from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time


class aviation():
     def __init__(self,root):
         self.root=root
         self.root.title("Aviation tickecting system")
         self.root.iconbitmap('fly.ico')
         self.root.geometry("1370x700+0+0")
         self.root.configure(background="gainsboro")

         #=======creating frmae================================================================================
         mainframe=Frame(self.root, bd=10,relief=RIDGE)
         mainframe.grid()

         #divinding top frame and bottom frame
         topframe1=Frame(mainframe,bd=10,relief=RIDGE,width=1350,height=100)
         topframe.grid()
         topfarme2=Frame(mainframe,bd=10,relief=RIDGE,width=1350,height=600)
         bottomframe.grid()

         #dividing in botton frame
         fL=Frame(bottomframe,bd=5, relief=RIDGE, width=440,height=560,pady=2)
         fL.grid(row=0,column=1)
         fR=Frame(bottomframe,bd=5,relief=RIDGE,width=890,height=570)
         fR.grid(row=0,column=0)

        #creating in frame in Right side
         fr1=Frame(fR,bd=5,width=885,height=210,relief=RIDGE)
         fr1.pack(side=TOP)
         fr2=Frame(fR,bd=5,width=885,height=350,pady=15,relief=RIDGE)
         fr2.pack(side=BOTTOM)

        #==== partation of frame=====
         f1 = Frame(fr1, bd=5, relief=RIDGE, width=250, height=200)
         f1.grid(row=0, column=0)

         f2 = Frame(fr1, bd=5, relief=RIDGE, width=310, height=200)
         f2.grid(row=0, column=1)

         f3 = Frame(fr1, bd=5,  relief=RIDGE, width=310, height=200)
         f3.grid(row=0, column=2)

         f4=Frame(fr2,bd=5,bg="light gray",relief=RIDGE,width=550,height=250)
         f4.grid(row=0,column=0)

         f5=Frame(fr2,bd=5,bg="light gray",relief=RIDGE, width=330,height=250)
         f5.grid(row=0,column=1)

     #=====creating frame in left======

         fl1 = Frame(fL, bd=5, bg="light gray", relief=RIDGE, width=430, height=450)
         fl1.pack(side=TOP)

         fl2 = Frame(fL, bd=5, bg="light gray", relief=RIDGE, width=430, height=100)
         fl2.pack(side=BOTTOM)

     #===TITLE==========

         title=Label( topframe,text="ticketing management system",bd=6,relief=GROOVE, fg="gray24",font=("courier",40,"bold"),justify="center",width=41)
         title.grid(row=0,column=0)

     #=======variables===
         Date1=StringVar()
         time1= StringVar()
         vehicle = StringVar()
         ticket_price = StringVar()
         child_ticket = StringVar()
         Adultticket = StringVar()
         from_destination= StringVar()
         To_destination= StringVar()
         To_destination = StringVar()
         fee_price=StringVar()
         Route=StringVar()
         Receipt_ref=StringVar()

         text_input=StringVar()
         global operator
         operator=""

         vehicle.set("")
         ticket_price.set("")
         child_ticket.set("")
         Adultticket.set("")
         from_destination.set("")
         To_destination.set("")
         To_destination.set("")
         fee_price.set("")
         Route.set("")
         Receipt_ref.set("")

         var1=IntVar()
         var2=IntVar()
         var3=IntVar()
         var4=IntVar()
         var5=StringVar()
         var6=StringVar()
         var7=StringVar()
         var8=IntVar()
         var9=IntVar()
         var10=IntVar()
         var11=IntVar()
         var12=IntVar()

         Tax=StringVar()
         subtotal=StringVar()
         total=StringVar()

         var1.set("0")
         var2.set("0")
         var3.set("0")
         var4.set("0")
         var5.set("0")
         var6.set("0")
         var7.set("0")
         var8.set("0")
         var9.set("0")
         var10.set("0")
         var11.set("0")
         var12.set("0")


         #=======================function decleration=======================================================================
         def iexit():
             iexit=tkinter.messagebox.askyesno("tickecting syetem","confirm if you want to quit")
             if iexit>0:
                 root.destroy()
                 return

         def reset():
             var1.set("0")
             var2.set("0")
             var3.set("0")
             var4.set("0")
             var5.set("0")
             var6.set("0")
             var7.set("0")
             var8.set("0")
             var9.set("0")
             var10.set("0")
             var11.set("0")
             var12.set("0")
             Tax.set("0")
             subtotal.set("0")
             total.set("0")
             vehicle.set("")
             ticket_price.set("")
             child_ticket.set("")
             Adultticket.set("")
             from_destination.set("")
             To_destination.set("")
             fee_price.set("")
             Route.set("")
             Receipt_ref.set("")

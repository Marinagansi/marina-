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
         self.root.configure(background="light gray")

         #=======creating frmae=======
         mainframe=Frame(self.root, bd=10,relief=RIDGE)
         mainframe.grid()

         #divinding top frame and bottom frame
         topframe=Frame(mainframe,bd=10,relief=RIDGE,width=1350,height=100)
         topframe.grid()
         bottomframe=Frame(mainframe,bd=10,relief=RIDGE,width=1350,height=600)
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


             # def btnclear():
             #     global opertaor
             #     opertaor=""
             #     text_Input.set("")
             #
             # def equal():
             #     global operator
             #     sumup=str(eval(operator))
             #     text_input.set("")
             #     operator=""

         def travel_cost():
                 if(var9.get()  == "pokhara" and var1.get()==1 and var4.get()==1):
                     tcost=float(1200.00)
                     single=float(var12.get())
                     Adult_Tax="rs" ,str("%.2f" % ((tcost * single) * 0.10))
                     Adult_fees="rs" ,str("%.2f" % (tcost * single))
                     Total_cost="rs" ,str("%.2f" % ((tcost * single) + ((tcost * single) * 0.10)))
                     Tax.set(Adult_Tax)
                     subtotal.set(Adult_fees)

                     vehicle.set("BUS")
                     ticket_price.set(Adult_fees)
                     child_ticket.set("No")
                     Adultticket.set("Yes")
                     from_destination.set("ktm")
                     To_destination.set("pokhara")
                     fee_price.set(Total_cost)
                     total.set(Total_cost)
                     Route.set("Direct")

                     x=random.randint(109,5876)
                     randomRef=str(x)
                     Receipt_ref.set("TFL"+ randomRef )
                 #
                 # elif(var9.get()  == "pokhara" and var1.get()==1 and var5.get()==1):
                 #     tcost=float(1200.00)
                 #     single=float(var12.get())
                 #     child_Tax="rs", str("%.2f" % ((tcost * 0.0))
                 #     child_fees="rs", str("%.2f" % (tcost * single))
                 #     Total_cost="rs", str("%.2f" % ((tcost * single) + ((tcost * 0.0)))
                 #     Tax.set(child_Tax)
                 #     subtotal.set(Child_fees)
                 #     vehicle.set("BUS")
                 #     ticket_price.set(child_fees)
                 #     child_ticket.set("YES")
                 #     Adultticket.set("NO")
                 #     from_destination.set("ktm")
                 #     To_destination.set("pokhara")
                 #     fee_price.set(Total_cost)
                 #     total.set(Total_cost)
                 #     Route.set("Direct")
                 #
                 #     x=random.randint(109,5876)
                 #     randomRef=str(x)
                 #     Receipt_ref.set("TFL"+ randomRef )



                 elif (var9.get()=="lumbini" and var1.get()==1 and var4.get()==1):
                     tcost=float(1300.00)
                     single=float(var12.get())
                     Adult_Tax="rs" ,str("%.2f" % ((tcost * single) * 0.10))
                     Adult_fees="rs" ,str("%.2f" % (tcost * single))
                     Total_cost="rs" ,str("%.2f" % ((tcost * single) + ((tcost * single) * 0.10)))
                     Tax.set(Adult_Tax)
                     subtotal.set(Adult_fees)
                     vehicle.set("BUS")
                     ticket_price.set(Adult_fees)
                     child_ticket.set("No")
                     Adultticket.set("Yes")
                     from_destination.set("ktm")
                     To_destination.set("lumbini")
                     fee_price.set(Total_cost)
                     total.set(Total_cost)
                     Route.set("Direct")

                     x=random.randint(109,5876)
                     randomRef=str(x)
                     Receipt_ref.set("TFL"+ randomRef )

                 elif (var9.get() == "lumbini" and var1.get() == 1 and var5.get() == 1):
                     tcost = float(1300.00)
                     single = float(var12.get())
                     child_Tax =  "rs", str("%.2f" % (tcost * 0))
                     child_fees = "rs", str("%.2f" % (tcost * single))
                     Total_cost = "rs", str("%.2f" % ((tcost * single) + ((tcost * 0)))
                     Tax.set (child_Tax)
                     subtotal.set(child_fees)
                     vehicle.set("BUS")
                     ticket_price.set(child_fees)
                     child_ticket.set("YES")
                     Adultticket.set("NO")
                     from_destination.set("ktm")
                     To_destination.set("pokhara")
                     fee_price.set(Total_cost)
                     total.set(Total_cost)
                     Route.set("Direct")

                     x = random.randint(109, 5876)
                     randomRef = str(x)
                     Receipt_ref.set("TFL" + randomRef)

                 elif (var9.get()=="chitwan" and var1.get()==1 and var4.get()==1):
                     tcost=float(1300.00)
                     single = float(var12.get())
                     Adult_Tax="rs" ,str("%.2f" % ((tcost * single) * 0.10))
                     Adult_fees="rs" ,str("%.2f" % (tcost * single))
                     Total_cost="rs" ,str("%.2f" % ((tcost * single) + ((tcost * single) * 0.10)))
                     Tax.set(Adult_Tax)
                     subtotal.set(Adult_fees)

                     vehicle.set("BUS")
                     ticket_price.set(Adult_fees)
                     child_ticket.set("No")
                     Adultticket.set("Yes")
                     from_destination.set("ktm")
                     To_destination.set("pokhara")
                     fee_price.set(Total_cost)
                     total.set(Total_cost)
                     Route.set("Direct")

                     x=random.randint(109,5876)
                     randomRef=str(x)
                     Receipt_ref.set("TFL"+ randomRef )

                 elif (var9.get() == "chitwan" and var1.get() == 1 and var5.get() == 1):
                     tcost = float(1200.00)
                     single = float(var12.get())
                     child_Tax = "rs", str("%.2f" % (tcost * 0))
                     child_fees = "rs", str("%.2f" % (tcost * single))
                     Total_cost = "rs", str("%.2f" % ((tcost * single) + ((tcost * 0)))
                     Tax.set(child_Tax)
                     subtotal.set(child_fees)
                     vehicle.set("BUS")
                     ticket_price.set(child_fees)
                     child_ticket.set("YES")
                     Adultticket.set("NO")
                     from_destination.set("ktm")
                     To_destination.set("pokhara")
                     fee_price.set(Total_cost)
                     total.set(Total_cost)
                     Route.set("Direct")

                     x = random.randint(109, 5876)
                     randomRef = str(x)
                     Receipt_ref.set("TFL" + randomRef)

                  elif (var9.get() == "pokhara" and var2.get() == 1 and var4.get() == 1):
                     tcost = float(1200.00)
                     single = float(var12.get())
                     Adult_Tax = "rs", str("%.2f" % ((tcost * single) * 0.10))
                     Adult_fees = "rs", str("%.2f" % (tcost * single))
                     Total_cost = "rs", str("%.2f" % ((tcost * single) + ((tcost * single) * 0.10)))
                     Tax.set(Adult_Tax)
                     subtotal.set(Adult_fees)

                     vehicle.set("micro")
                     ticket_price.set(Adult_fees)
                     child_ticket.set("No")
                     Adultticket.set("Yes")
                     from_destination.set("ktm")
                     To_destination.set("pokhara")
                     fee_price.set(Total_cost)
                     total.set(Total_cost)
                     Route.set("Direct")

                     x = random.randint(109, 5876)
                     randomRef = str(x)
                     Receipt_ref.set("TFL" + randomRef)

                     elif (var9.get() == "pokhara" and var2.get() == 1 and var5.get() == 1):
                     tcost = float(1200.00)
                     single = float(var12.get())
                     child_Tax = "rs", str("%.2f" % ((tcost * 0))
                     child_fees = "rs", str("%.2f" % (tcost * single))
                     Total_cost = "rs", str("%.2f" % ((tcost * single) + ((tcost * 0)))
                     Tax.set(child_Tax)
                     subtotal.set(child_fees)
                     vehicle.set("micro")
                     ticket_price.set(child_fees)
                     child_ticket.set("YES")
                     Adultticket.set("NO")
                     from_destination.set("ktm")
                     To_destination.set("pokhara")
                     fee_price.set(Total_cost)
                     total.set(Total_cost)
                     Route.set("Direct")

                     x = random.randint(109, 5876)
                     randomRef = str(x)
                     Receipt_ref.set("TFL" + randomRef)

                     elif (var9.get() == "lumbini" and var2.get() == 1 and var4.get() == 1):
                     tcost = float(1300.00)
                     single = float(var12.get())
                     Adult_Tax = "rs", str("%.2f" % ((tcost * single) * 0.10))
                     Adult_fees = "rs", str("%.2f" % (tcost * single))
                     Total_cost = "rs", str("%.2f" % ((tcost * single) + ((tcost * single) * 0.10)))
                     Tax.set(Adult_Tax)
                     subtotal.set(Adult_fees)
                     vehicle.set("micro")
                     ticket_price.set(Adult_fees)
                     child_ticket.set("No")
                     Adultticket.set("Yes")
                     from_destination.set("ktm")
                     To_destination.set("pokhara")
                     fee_price.set(Total_cost)
                     total.set(Total_cost)
                     Route.set("Direct")

                     x = random.randint(109, 5876)
                     randomRef = str(x)
                     Receipt_ref.set("TFL" + randomRef)

                 elif (var9.get() == "lumbini" and var2.get() == 1 and var5.get() == 1):
                     tcost = float(1300.00)
                     single = float(var12.get())
                     child_Tax = "rs", str("%.2f" % ((tcost * 0))
                     child_fees = "rs", str("%.2f" % (tcost * single))
                     Total_cost = "rs", str("%.2f" % ((tcost * single) + ((tcost * 0)))
                     Tax.set(child_Tax)
                     subtotal.set(child_fees)
                     vehicle.set("micro")
                     ticket_price.set(child_fees)
                     child_ticket.set("YES")
                     Adultticket.set("NO")
                     from_destination.set("ktm")
                     To_destination.set("pokhara")
                     fee_price.set(Total_cost)
                     total.set(Total_cost)
                     Route.set("Direct")

                     x = random.randint(109, 5876)
                     randomRef = str(x)
                     Receipt_ref.set("TFL" + randomRef)

                 elif (var9.get() == "chitwan" and var2.get() == 1 and var4.get() == 1):
                     tcost = float(1300.00)
                     single = float(var12.get())
                     Adult_Tax = "rs", str("%.2f" % ((tcost * single) * 0.10))
                     Adult_fees = "rs", str("%.2f" % (tcost * single))
                     Total_cost = "rs", str("%.2f" % ((tcost * single) + ((tcost * single) * 0.10)))
                     Tax.set(Adult_Tax)
                     subtotal.set(Adult_fees)

                     vehicle.set("micro")
                     ticket_price.set(Adult_fees)
                     child_ticket.set("No")
                     Adultticket.set("Yes")
                     from_destination.set("ktm")
                     To_destination.set("pokhara")
                     fee_price.set(Total_cost)
                     total.set(Total_cost)
                     Route.set("Direct")

                     x = random.randint(109, 5876)
                     randomRef = str(x)
                     Receipt_ref.set("TFL" + randomRef)

                 elif (var9.get() == "chitwan" and var2.get() == 1 and var5.get() == 1):
                     tcost = float(1200.00)
                     single = float(var12.get())
                     child_Tax = "rs", str("%.2f" % ((tcost * 0))
                     child_fees = "rs", str("%.2f" % (tcost * single))
                     Total_cost = "rs", str("%.2f" % ((tcost * single) + ((tcost * 0)))
                     Tax.set(child_Tax)
                     subtotal.set(child_fees)
                     vehicle.set("micro")
                     ticket_price.set(child_fees)
                     child_ticket.set("YES")
                     Adultticket.set("NO")
                     from_destination.set("ktm")
                     To_destination.set("pokhara")
                     fee_price.set(Total_cost)
                     total.set(Total_cost)
                     Route.set("Direct")

                     x = random.randint(109, 5876)
                     randomRef = str(x)
                     Receipt_ref.set("TFL" + randomRef)

                     def sbtn():
                      if (var10.get()==1):
                        var12.set("")
                        entrysingle.focus()
                        entrysingle.configure(state=NORMAL)
                        var11.set(0)
                        entryreturn.configure(state=DISABLED)
                        var6.set("0")
                      elif var10.get()==0:
                        entrysingle.configured(state=DISABLED)
                        var12.set("0")

         def rbtn():
                    if (var11.get() == 1):
                        var6.set("")
                        entryreturn.focus()
                        entryreturn.configure(state=NORMAL)
                        var10.set(0)
                        entrysingle.configure(state=DISABLED)
                        var12.set("0")
                    elif var11.get() == 0:
                        entryreturn.configured(state=DISABLED)
                        var6.set("0")












#========label widget==============================================================================================
         lblreceipt=Label( fl1,text="travelling ticket",bd=4,relief=GROOVE, fg="gray14",font=("courier",30,"bold"),justify="center")
         lblreceipt.grid(row=0,column=0)

         lblvechicle1 = Label(fl2, text="vechile", relief=GROOVE,font=("courier", 14, ), width=8,justify="center")
         lblvechicle1.grid(row=0, column=0)
         lblvechicle2= Label(fl2, relief=GROOVE, font=("courier", 14,), width=8, justify="center",textvariable=vehicle)
         lblvechicle2.grid(row=1, column=0)

         lblprice1 = Label(fl2, text="price",relief="sunken", font=("courier", 14,), width=8, justify="center")
         lblprice1.grid(row=0, column=1)
         lblprice2 = Label(fl2, relief="sunken", font=("courier", 14,), width=8, justify="center",textvariable=ticket_price)
         lblprice2.grid(row=1, column=1)

         lbladult1 = Label(fl2, text="Adult", relief="sunken", font=("courier", 14,), width=8, justify="center")
         lbladult1.grid(row=0, column=2)
         lbladult2 = Label(fl2, relief="sunken", font=("courier", 14,), width=8, justify="center",textvariable=Adultticket)
         lbladult2.grid(row=1, column=2)

         lblchild1 = Label(fl2, text="child", relief="sunken", font=("courier", 14,), width=8, justify="center")
         lblchild1.grid(row=0, column=3)
         lblchild2 = Label(fl2, relief="sunken", font=("courier", 14,), width=8, justify="center",textvariable=  child_ticket)
         lblchild2.grid(row=1, column=3)


         lblsp=Label(fl2,bg="light gray",height=2,width=49,font=("arial", 7))
         lblsp.grid(row=2,column=0,columnspan=4)

         # ========labelwidget====================================================================================
         lblfrom1 = Label(fl2, text="from", relief="sunken", font=("courier", 14,), width=8, justify="center")
         lblfrom1.grid(row=3, column=1)
         lblfrom2 = Label(fl2, relief="sunken", font=("courier", 14,), width=8, justify="center")
         lblfrom2.grid(row=3, column=2)

         lblto1 = Label(fl2, text="TO", relief="sunken", font=("courier", 14,), width=8, justify="center")
         lblto1.grid(row=4,column=1)
         lblto2 = Label(fl2, relief="sunken", font=("courier", 14,), width=8, justify="center")
         lblto2.grid(row=4, column=2)

         lblRs1 = Label(fl2, text="TO", relief="sunken", font=("courier", 14,), width=8, justify="center")
         lblRs1.grid(row=5, column=1)
         lblRs2 = Label(fl2, relief="sunken", font=("courier", 14,), width=8, justify="center")
         lblRs2.grid(row=5, column=2)

         #=====space bar=====
         lblsp1=Label(fl2,bg="light gray",height=2,width=49,font=("arial", 7))
         lblsp1.grid(row=6,column=0,columnspan=4)

        #======label widget=======
         lblRefno1=Label(fl2,text="Ref No",relief="sunken",font=("courier",14),width=8,justify="center")
         lblRefno1.grid(row=7,column=0)
         lblRefno2 = Label(fl2, relief="sunken", font=("courier", 14,), width=8, justify="center",textvariable=Receipt_ref)
         lblRefno2.grid(row=8, column=0)

         lbltime1 = Label(fl2, text="Time", relief="sunken", font=("courier", 14),width=8, justify="center")
         lbltime1.grid(row=7, column=1)
         lbltime2 = Label(fl2, relief="sunken", font=("courier", 14,), textvariable=time1, width=8, justify="center",)
         lbltime2.grid(row=8, column=1)

         lbldate1 = Label(fl2, text="Date", relief="sunken", font=("courier", 14), width=8, justify="center")
         lbldate1.grid(row=7, column=2)
         lbldate2 = Label(fl2, relief="sunken", font=("courier", 14,), width=8, textvariable=Date1, justify="center")
         lbldate2.grid(row=8, column=2)

         lblroute1= Label(fl2, text="Route", relief="sunken", font=("courier", 14), width=8, justify="center")
         lblroute1.grid(row=7, column=3)
         lblroute2 = Label(fl2, relief="sunken", font=("courier", 14,), width=8, justify="center",textvariable=Route)
         lblroute2.grid(row=8, column=3)
         #===========space=====
         lblsp2=Label(fl2, font=("courier", 14), width=8, justify="center",bg="light gray")
         lblsp2.grid(row=9,column=0,columnspan=4)

         #===================================================================================================
         Date1.set(time.strftime("%d/%m/%y"))
         time1.set(time.strftime("%H:%M:%S"))
         #===================================================================================================

         lblvechicle=Label(f1, text="class",font=("courier", 14,),bd=8)
         lblvechicle.grid(row=0,column=0,sticky=W)


         checkvechile=Checkbutton(f1, font=("courier", 22,"bold"),text="BUS", variable=var1, onvalue=1,offvalue=0)
         checkvechile.grid(row=1,column=0,sticky=W)

         checkvechicle1 = Checkbutton(f1, font=("courier", 22,"bold"), text="micro",variable=var2, onvalue=1, offvalue=0)
         checkvechicle1.grid(row=2, column=0, sticky=W)

         checkvechicle2 = Checkbutton(f1, font=("courier", 22,"bold") , text="scorpio", variable=var3, onvalue=1,
                                      offvalue=0)
         checkvechicle2.grid(row=3, column=0, sticky=W)

         #==========================================================================================


         lblselectdestination=Label(f2, text="select destination",font=("courier", 14,))
         lblselectdestination.grid(row=0,column=0,sticky=W,columnspan=2)
         lbldestination=Label(f2, text=" Destination",font=("courier", 14,)).grid(row=1,column=0,sticky=W)
         comdestination=ttk.Combobox(f2,font=("courier", 14,), textvariable=var9, state="readonly",width=10)
         comdestination['value']=('',"pokhara","lumbini","chitwan","ilam",)
         comdestination.current(0)
         comdestination.grid(row=1,column=1)

         checkAdult = Checkbutton(f2, font=("courier", 22, "bold"), text="Adult", variable=var4,
                                      onvalue=1, offvalue=0)
         checkAdult.grid(row=2, column=0, sticky=W)

         checkchild = Checkbutton(f2, font=("courier", 22, "bold"), text="Child",  variable=var5,
                                      onvalue=1,
                                      offvalue=0)
         checkchild.grid(row=3, column=0, sticky=W)

         # ========================================================================================================

         lblticket=Label(f3, text="ticket type", font=('courier', 14), ).grid(row=0,column=0,sticky=W)

         chksingle=Checkbutton(f3,font=('courier',22,"bold"),text="single",variable=var10,onvalue=1,offvalue=0)
         chksingle.grid(row=1,column=0,sticky=W)

         entrysingle=Entry(f3,font=('courier', 15, ), bd=8,textvariable=var12,width=8).grid(row=1,column=1)

         chkreturn = Checkbutton(f3, font=('courier', 22, "bold"), bd=8,text="Return", variable=var11, onvalue=1, offvalue=0,)
         chkreturn.grid(row=2, column=0, sticky=W)

         entryreturn= Entry(f3, font=('courier', 15,),bd=8, textvariable=var6, width=8).grid(row=2, column=1)

         comment=Label(f3,text="comment",font=('courier', 22, "bold")).grid(row=3,column=0,sticky=W)

         entrycomment=Entry(f3,font=('courier', 15, ), bd=8,textvariable=var7,width=8).grid(row=3,column=1)


        #=================================================================================================
         lbltax=Label(f4,text="state tax",font=('courier', 22, "bold"), bg="light gray").grid(row=0,column=0,sticky=W)
         entrtax=Entry(f4,font=('courier', 15, ),textvariable=Tax,).grid(row=0,column=1)

         lbltotal = Label(f4, text="sub total", font=('courier', 22, "bold"), bg="light gray").grid(row=2, column=0,
                                                                                                  sticky=W)
         entrtotal = Entry(f4, font=('courier', 15,),  textvariable=subtotal, ).grid(row=2, column=1)

         lblcost = Label(f4, text="total cost", font=('courier', 22, "bold"), bg="light gray").grid(row=4, column=0,
                                                                                                  sticky=W)
         entrcost = Entry(f4, font=('courier', 15,),  textvariable=total, ).grid(row=4, column=1)

         #======buttons======================================================================================

         ttlbtn=Button(fl2, text="total", relief="sunken", bg="black",font=("courier", 14), width=8,height=1, justify="center", command=travel_cost)
         ttlbtn.grid(row=10,column=0)

         clearbtn = Button(fl2, text="clear", relief="sunken", font=("courier", 14), width=8, height=1, justify="center")
         clearbtn.grid(row=10, column=1)

         resetbtn = Button(fl2, text="reset", relief="sunken", font=("courier", 14), width=8, height=1, justify="center",command=reset)
         resetbtn.grid(row=10, column=2)

         exitbtn = Button(fl2, text="exit", relief="sunken", font=("courier", 14), width=8, height=1,
                           justify="center", command=iexit)
         exitbtn.grid(row=10, column=3)

#=============================calculator==========================================================================
         e = Entry(f5, width=25, borderwidt=10)
         e.grid(row=0, column=0, columnspan=12, padx=5,pady=5)

         def button_click(number):
             current = e.get()
             e.delete(0, END)
             e.insert(0, str(current) + str(number))

         def button_clear():
             e.delete(0, END)

         def button_add():
             first_number = e.get()
             global f_num
             global operation
             operation = "add"
             f_num = int(first_number)
             e.delete(0, END)

         def button_sub():
             first_number = e.get()
             global f_num
             global operation
             operation = "sub"
             f_num = int(first_number)
             e.delete(0, END)

         def button_multi():
             first_number = e.get()
             global f_num
             global operation
             operation = "multi"
             f_num = int(first_number)
             e.delete(0, END)

         def button_div():
             first_number = e.get()
             global f_num
             global operation
             operation = "div"
             f_num = int(first_number)
             e.delete(0, END)

         def button_equal():
             second_number = e.get()
             e.delete(0, END)
             if operation == "add":
                 e.insert(0, f_num + int(second_number))
             if operation == "sub":
                 e.insert(0, f_num - int(second_number))
             if operation == "multi":
                 e.insert(0, f_num * int(second_number))
             if operation == "div":
                 e.insert(0, f_num / int(second_number))

         button_1 = Button(f5, text="1", padx=7, pady=6, font=('courier', 16, "bold"), command=lambda: button_click(1))
         button_2 = Button(f5, text="2",padx=7, pady=6, font=('courier', 16, "bold"), command=lambda: button_click(2))
         button_3 = Button(f5, text="3", padx=7, pady=6, font=('courier', 16, "bold"), command=lambda: button_click(3))

         button_4 = Button(f5, text="4",padx=7, pady=6, font=('courier', 16, "bold"),command=lambda: button_click(4))
         button_5 = Button(f5, text="5", padx=7, pady=6, font=('courier', 16, "bold"),command=lambda: button_click(5))
         button_6 = Button(f5, text="6", padx=7, pady=6, font=('courier', 16, "bold"), command=lambda: button_click(6))
         button_7 = Button(f5, text="7", padx=7, pady=6, font=('courier', 16, "bold"), command=lambda: button_click(7))
         button_8 = Button(f5, text="8",padx=7, pady=6, font=('courier', 16, "bold"), command=lambda: button_click(8))
         button_9 = Button(f5, text="9", padx=7, pady=6, font=('courier', 16, "bold"),command=lambda: button_click(9))
         button_0 = Button(f5, text="0",padx=7, pady=6, font=('courier', 16, "bold"),command=lambda: button_click(0))
         button_add = Button(f5, text="+", padx=7, pady=6, font=('courier', 16, "bold"), command=button_add)
         button_equal = Button(f5, text="=", padx=7, pady=6, font=('courier', 16, "bold"), command=button_equal)
         button_clear = Button(f5, text="c",padx=7, pady=6, font=('courier', 16, "bold"), command=button_clear)
         button_sub = Button(f5, text="-", padx=7, pady=6, font=('courier', 16, "bold"),command=button_sub)
         button_multi = Button(f5, text="*", padx=7, pady=6, font=('courier', 16, "bold"), command=button_multi)
         button_div = Button(f5, text="/", padx=7, pady=6, font=('courier', 16, "bold"), command=button_div)

         button_1.grid(row=1, column=0)
         button_2.grid(row=1, column=1)
         button_3.grid(row=1, column=2)

         button_4.grid(row=2, column=0)
         button_5.grid(row=2, column=1)
         button_6.grid(row=2, column=2)

         button_7.grid(row=3, column=0)
         button_8.grid(row=3, column=1)
         button_9.grid(row=3, column=2)

         button_0.grid(row=4, column=0)
         button_sub.grid(row=2, column=3)
         button_multi.grid(row=3, column=3)
         button_add.grid(row=1, column=3)
         button_equal.grid(row=4,column=1)
         button_clear.grid(row=4, column=3)
         button_div.grid(row=4, column=2)



class aviation():
    pass
    root=Tk()
    obj=aviation(root)
    root.mainloop()
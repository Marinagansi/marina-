from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox




class hospital():
    def __init__(self,root):
         self.root=root
         self.root.title(" hospital management system")
         self.root.geometry("1370x800+0+0")
         title=Label(root,text="Hospital management system",bd=6,relief=GROOVE, font=("times new roman",50,"bold"),bg="blUe", fg="yellow")
         title.pack(side=TOP,fill=X)
         frame=Frame(self.root, bd=9,relief=RIDGE,padx=20,bg="powder blue").place(x=10,y=100,width=1350, height=400)
         #=======dataframeleft=====
         Dataframeleft=LabelFrame(frame,text="patient information", bd=6,  bg="powder blue", fg="green", font=("times new roman",10,"bold"))
         Dataframeleft.place(x=30,y=130,width=700,height=350)

         # =====creating combobox========
         lblmember=Label(Dataframeleft, text="Name of tablet",bg="powder blue",font=("arial",15)).grid(row=0,column=0,sticky=W)
         comember=ttk.Combobox(Dataframeleft,font=("arial",10),width=27,state="readonly")
         comember["value"]=("corona vaccine", "caplets","pills","odt")
         comember.grid(row=0,column=1,sticky=W)
#====creating text column===================================================================================
         lblrefenceno=Label(Dataframeleft,text="Refence no",bg="powder blue" ,font=("arial",15),padx=2,pady=3).grid(row=1,column=0,sticky=W)
         txtrefenceno=Entry(Dataframeleft,font=("arial",10),width=30)
         txtrefenceno.grid(row=1,column=1,sticky=W)

         lbldose= Label(Dataframeleft, text="Dose", bg="powder blue", font=("arial", 15), padx=2,
                              pady=3).grid(row=2, column=0, sticky=W)
         txtdose = Entry(Dataframeleft, font=("arial", 10), width=30)
         txtdose.grid(row=2, column=1, sticky=W)

         lblnoftablet = Label(Dataframeleft, text="No of tablet", bg="powder blue", font=("arial", 15), padx=2,
                         pady=3).grid(row=3, column=0, sticky=W)
         txtnooftablet = Entry(Dataframeleft, font=("arial", 10), width=30)
         txtnooftablet.grid(row=3, column=1, sticky=W)

         lbllot = Label(Dataframeleft, text="lot", bg="powder blue", font=("arial", 15), padx=2,
                              pady=3).grid(row=4, column=0, sticky=W)
         txtlot = Entry(Dataframeleft, font=("arial", 10), width=30)
         txtlot.grid(row=4, column=1, sticky=W)


         lblissuedate = Label(Dataframeleft, text="Issue date", bg="powder blue", font=("arial", 15), padx=2,
                              pady=3).grid(row=5, column=0,sticky=W)
         txtissuedate = Entry(Dataframeleft, font=("arial", 10), width=30)
         txtissuedate.grid(row=5, column=1, sticky=W)


         lblexpdate=Label(Dataframeleft, text="exp date", bg="powder blue", font=("arial", 15), padx=2,
                              pady=3).grid(row=6, column=0,sticky=W)
         txtexpdate= Entry(Dataframeleft, font=("arial", 10), width=30)
         txtexpdate.grid(row=6, column=1, sticky=W)


         lbldailydose=Label(Dataframeleft, bg="powder blue"  ,text="Daily dose",font=("arial",15),padx=2,pady=3).grid(row=7
                                                                                               ,column=0,sticky=W)
         textdailydose=Entry(Dataframeleft,font=("arial",10),width=30)
         textdailydose.grid(row=7,column=1,sticky=W)

         lblsideeffect=Label(Dataframeleft, bg="powder blue"  ,text="side effect",font=("arial",15),padx=2,pady=3).grid(row=8,column=0,sticky=W)
         textsideeffect=Entry(Dataframeleft,font=("arial",10),width=30)
         textsideeffect.grid(row=8,column=1,sticky=W)

         # ====creating COMBOBOX======================================================================
         lblgender=Label(Dataframeleft, text="gender", bg="powder blue",font=("arial",15)).grid(row=0,column=3,sticky=W)
         cogender = ttk.Combobox(Dataframeleft, font=("arial", 10), width=25, state="readonly")
         cogender["value"] = ("female", "male", "other")
         cogender.grid(row=0, column=4, sticky=W)
         #==============================================================================================


         lblbloodpressure = Label(Dataframeleft, bg="powder blue", text="Blood pressure", font=("arial", 15), padx=2, pady=3).grid(
              row=1, column=3,sticky=W)
         textbloodpressure= Entry(Dataframeleft, font=("arial", 10), width=27)
         textbloodpressure.grid(row=1, column=4, sticky=W)

         lblstorageadvice = Label(Dataframeleft, bg="powder blue", text="storage advice", font=("arial", 15), padx=2, pady=3).grid(
              row=2, column=3,sticky=W)
         textstorageadvice = Entry(Dataframeleft, font=("arial", 10), width=27)
         textstorageadvice.grid(row=2, column=4, sticky=W)

         lblmedication = Label(Dataframeleft, bg="powder blue", text="Medication", font=("arial", 15), padx=2, pady=3).grid(
              row=3, column=3,sticky=W)
         textmedication = Entry(Dataframeleft, font=("arial", 10), width=27)
         textmedication.grid(row=3, column=4, sticky=W)

         lblpatientid = Label(Dataframeleft, bg="powder blue", text="Patient Id", font=("arial", 15), padx=2,
                               pady=3).grid(
              row=4, column=3,sticky=W)
         textpatientid= Entry(Dataframeleft, font=("arial", 10), width=27)
         textpatientid.grid(row=4, column=4, sticky=W)

         lblnhsnumber = Label(Dataframeleft, bg="powder blue", text="NHS number", font=("arial", 15), padx=2,
                               pady=3).grid(
              row=5, column=3,sticky=W)
         textnhsnumber= Entry(Dataframeleft, font=("arial", 10), width=27)
         textnhsnumber.grid(row=5, column=4, sticky=W)

         lblpatientname = Label(Dataframeleft, bg="powder blue", text="Patient name", font=("arial", 15), padx=2,
                               pady=3).grid(
              row=6, column=3,sticky=W)
         textpatientname = Entry(Dataframeleft, font=("arial", 10), width=27)
         textpatientname.grid(row=6, column=4, sticky=W)


         lblDOB= Label(Dataframeleft, bg="powder blue", text="DOB", font=("arial", 15), padx=2,
                               pady=3).grid(
              row=7, column=3,sticky=W)
         textDOB = Entry(Dataframeleft, font=("arial", 10), width=27)
         textDOB.grid(row=7, column=4, sticky=W)



         lbladdress= Label(Dataframeleft, bg="powder blue", text="address", font=("arial", 15), padx=2,
                               pady=3).grid(
              row=8, column=3,sticky=W)
         textaddress= Entry(Dataframeleft, font=("arial", 10), width=27)
         textaddress.grid(row=8, column=4, sticky=W)


         #=====dATA FRAME RIGHT=======================================================================================
         Dataframeright=LabelFrame(frame,text="prescription",bd=6,bg="powder blue",fg="green",font=("times new romen",10, "bold"))
         Dataframeright.place(x=750,y=130,width=590,height=350)
         self.txtprescription=Text(Dataframeright,bg="white",fg="green",font=("times new romen",10, "bold")
                                    ,width=80,height=19,padx=5,pady=6)

         self.txtprescription.grid(row=0,column=0)

         # ======button frame===========================================================================================
         buttonframe = LabelFrame(frame, bd=6, bg="powder blue")
         buttonframe.place(x=10, y=505, width=1350, height=90)

#====================adding button============================================================================

         btnprescripton=Button(buttonframe,text="prescription",font=("arial",12,"bold"), width=20,height=2,
                               bg="light grey",padx=4,pady=6)
         btnprescripton.grid(row=0,column=0)


         btnprescriptondata=Button(buttonframe,text="prescription data",font=("arial",12,"bold"), width=20,height=2,
                               bg="light grey",padx=4,pady=6)
         btnprescriptondata.grid(row=0,column=1)


         btnupdate=Button(buttonframe,text="update",font=("arial",12,"bold"), width=20,height=2,
                               bg="light grey",padx=4,pady=6)
         btnupdate.grid(row=0,column=2)


         btndelete=Button(buttonframe,text="delete",font=("arial",12,"bold"), width=20,height=2,
                               bg="light grey",padx=4,pady=6)
         btndelete.grid(row=0,column=3)


         btnclear=Button(buttonframe,text="clear",font=("arial",12,"bold"), width=20,height=2,
                               bg="light grey",padx=4,pady=6)
         btnclear.grid(row=0,column=4)


         btnexit=Button(buttonframe,text="exit",font=("arial",12,"bold"), width=20,height=2,
                               bg="light grey",padx=4,pady=6)
         btnexit.grid(row=0,column=5)

         #==============table==============================================================================

         # ====information frame================================================================================
         infoframe = LabelFrame(frame, bd=6, bg="powder blue")
         infoframe.place(x=10, y=595, width=1350, height=190)




         #======================scrollbar============================================================


         scroll_x=ttk.Scrollbar(infoframe,orient=HORIZONTAL)
         scroll_y=ttk.Scrollbar(infoframe,orient=VERTICAL)
         self.hospital_table=ttk.Treeview(infoframe,column=("nameoftable","ref","dose","nooftablet","lot","issuedate","expdate",
                          "dailydose", "storage","nhsnumber","pname","DOB","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)

         scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
         scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

         self.hospital_table.heading("nameoftable",text="Name of table")
         self.hospital_table.heading("ref", text="reference no")
         self.hospital_table.heading("dose", text="Dose")
         self.hospital_table.heading("nooftablet", text="Name of tablet")
         self.hospital_table.heading("lot", text="lot")
         self.hospital_table.heading("issuedate", text="issue date")
         self.hospital_table.heading("expdate", text="Exp date")
         self.hospital_table.heading("dailydose", text="Daily dose")
         self.hospital_table.heading("storage", text="storage")
         self.hospital_table.heading("nhsnumber", text="NHS number")
         self.hospital_table.heading("pname", text="patient name")
         self.hospital_table.heading("DOB", text="DOB")
         self.hospital_table.heading("address", text="address")

         self.hospital_table["show"]="headings"


         self.hospital_table.column("nameoftable",width=100)
         self.hospital_table.column("ref", width=100)
         self.hospital_table.column("dose", width=100)
         self.hospital_table.column("nooftablet", width=100)
         self.hospital_table.column("lot", width=100)
         self.hospital_table.column("issuedate", width=100)
         self.hospital_table.column("expdate", width=100)
         self.hospital_table.column("dailydose", width=100)
         self.hospital_table.column("storage", width=100)
         self.hospital_table.column("nhsnumber", width=100)
         self.hospital_table.column("pname", width=100)
         self.hospital_table.column("DOB", width=100)
         self.hospital_table.column("address", width=100)

         self.hospital_table.pack(fill=BOTH, expand=1)

         #==============================fuctinality declaration======================================================
        # def iprescriptiondata(self):
        #      if self.nameoftablets.get()=="" or ref.get()=="":
        #           messagebox.showerror("error","All flieds are required")































class hospital():
    pass
    root=Tk()
    obj=hospital(root)
    root.mainloop()
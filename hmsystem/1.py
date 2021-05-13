from tkinter import*
from PIL import ImageTk,Image
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("ABC hospital")
root.geometry("1370x800+0+0")
root.iconbitmap("hlogo.ico")
# root.resizable(False,False)
my_image=ImageTk.PhotoImage(Image.open("pm.jpg"))
my_label=Label(image=my_image)
image1=Label(root,image=my_image).place(x=0,y=0,relwidth=1,relheight=1)

conn=sqlite3.connect("record.db")


c= conn.cursor()
'''
c.execute ("""CREATE TABLE record1(
            name_of_tablet text,
            refence_no text,
            dose integer,
            lot text,
            issue_date text,
            exp_date text,
            daily_dose integer,
            side_effect text,
            gender text,
            blood_pressure text,
            storage_advice  text,
            medication text,
            patient_Id integer,
            NHS_number integer,
            patient_name text,
            dob integer,
            address text
)
 """)
print("table sucesss")
conn.commit()
conn.close()
'''


def prescriton():
    conn = sqlite3.connect("record.db")

    c=conn.cursor()
    c.execute("INSERT INTO record1 VALUES (:name_of_tablet, :refence_no, :dose, :lot, :issue_date,:exp_date,:daily_dose,:side_effect,:gender,:blood_pressure ,:storage_advice,:medication,:patient_Id,:NHS_number ,:patient_name,:dob, :address  )",{
       'name_of_tablet':comember.get(),
       'refence_no': txtrefenceno.get(),
       'dose':txtdose.get(),
       'lot':txtlot.get(),
       'issue_date':txtissuedate.get(),
       'exp_date':txtexpdate.get(),
       'daily_dose': textdailydose.get(),
       'side_effect':textsideeffect.get(),
       'gender':cogender.get(),
       'blood_pressure':textbloodpressure.get(),
       'storage_advice': textstorageadvice.get(),
       'medication': textmedication.get(),
       'patient_Id':textpatientid.get(),
       'NHS_number':textnhsnumber.get(),
       'patient_name':textpatientid.get(),
       'dob':textDOB.get(),
       'address':textaddress.get()
    })
    print('succesful')
    conn.commit()
    conn.close()
#============================================================
def display():
    conn= sqlite3.connect("record.db")

    c=conn.cursor()
    c.execute("SELECT *, oid FROM record1")
    records= c.fetchall()
    print_records=''
    for record in records:
        print_records += "name:-"+""+""+str(record[0]) +'      ' + str(record[1]) + '      ' + str(record[2]) +'\n'

    query_label=Label(root,text=print_records)
    query_label.place(x=20,y=640)

    conn.commit()
    conn.close()

def clear():
    comember.delete(0,END)
    txtrefenceno.delete(0,END)
    txtdose.delete(0,END)
    txtlot.delete(0,END)
    txtissuedate.delete(0,END)
    txtexpdate.delete(0,END)
    textdailydose.delete(0,END)
    textsideeffect.delete(0,END)
    cogender.delete(0,END)
    textbloodpressure.delete(0,END)
    textstorageadvice.delete(0,END)
    textmedication.delete(0,END)
    textpatientid.delete(0,END)
    textnhsnumber.delete(0,END)
    textpatientid.delete(0,END)
    textDOB.delete(0,END)
    textaddress.delete(0,END)





def exit():
    iexit = messagebox.askyesno("pharmecy management", "confirm if you want to quit")
    if iexit > 0:
        root.destroy()
        return



def hospital():
         # global my_hospital
         # top= Toplevel()

         root.title(" hospital management system")
         root.geometry("1370x800+0+0")
         title=Label(root,text="Hospital management system",bd=6,relief=GROOVE, font=("times new roman",50,"bold"),bg="powder blue", fg="black")
         title.pack(side=TOP,fill=X)
         frame=Frame(root, bd=9,relief=RIDGE,padx=20,bg="powder blue").place(x=10,y=100,width=1350, height=400)
         #=======dataframeleft===========================================================
         Dataframeleft=LabelFrame(root,text="patient information", bd=6,  bg="powder blue", fg="green", font=("times new roman",10,"bold"))
         Dataframeleft.place(x=30,y=130,width=700,height=350)

        #creating global
         global comember
         global txtrefenceno
         global txtdose
         global txtnooftablet
         global  txtlot
         global txtissuedate
         global  txtexpdate
         global  textdailydose
         global  textsideeffect
         global  cogender
         global  textbloodpressure
         global   textstorageadvice
         global  textmedication
         global textnhsnumber
         global  textpatientid
         global textDOB
         global textaddress


         # =====creating combobox======================================================================
         lblmember=Label(Dataframeleft, text="Name of tablet",bg="powder blue",font=("arial",15)).grid(row=0,column=0,sticky=W)
         comember=ttk.Combobox(Dataframeleft,font=("arial",10),width=27,state="readonly")
         comember["value"] = ("covid", "antibiotic", "pills")
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
         cogender["value"] = ("female", "male")
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



         # ======button frame===========================================================================================
         buttonframe = LabelFrame(root, bd=6, bg="powder blue")
         buttonframe.place(x=10, y=505, width=1350, height=90)

         #====================adding button============================================================================

         btnprescripton=Button(buttonframe,text="prescription",font=("arial",12,"bold"), width=20,height=2,
                               bg="light grey",padx=4,pady=6,command=prescriton)
         btnprescripton.grid(row=0,column=0)


         btnprescriptondata=Button(buttonframe,text="prescription data",font=("arial",12,"bold"), width=20,height=2,
                               bg="light grey",padx=4,pady=6,command=display)
         btnprescriptondata.grid(row=0,column=1)


         btnupdate=Button(buttonframe,text="update",font=("arial",12,"bold"), width=20,height=2,
                               bg="light grey",padx=4,pady=6)
         btnupdate.grid(row=0,column=2)


         btndelete=Button(buttonframe,text="delete",font=("arial",12,"bold"), width=20,height=2,
                               bg="light grey",padx=4,pady=6)
         btndelete.grid(row=0,column=3)


         btnclear=Button(buttonframe,text="clear",font=("arial",12,"bold"), width=20,height=2,
                               bg="light grey",padx=4,pady=6,command=clear)
         btnclear.grid(row=0,column=4)


         btnexit=Button(buttonframe,text="exit",font=("arial",12,"bold"), width=20,height=2,
                               bg="light grey",padx=4,pady=6,command=exit)
         btnexit.grid(row=0,column=5)

         #==============table==============================================================================

         # ====information frame================================================================================
         infoframe = LabelFrame(root, bd=6, bg="powder blue")
         infoframe.place(x=10, y=595, width=1350, height=190)
         # =====dATA FRAME RIGHT=======================================================================================
         Dataframeright = LabelFrame(root, text="prescription", bd=6, bg="powder blue", fg="green",
                                     font=("times new romen", 10, "bold"))
         Dataframeright.place(x=750, y=130, width=590, height=350)
         txtprescription = Text(Dataframeright, bg="white", fg="green", font=("times new romen", 10, "bold")
                                , width=80, height=19, padx=5, pady=6)

         txtprescription.grid(row=0, column=0)

         #======================scrollbar============================================================


         scroll_x=ttk.Scrollbar(infoframe,orient=HORIZONTAL)
         scroll_y=ttk.Scrollbar(infoframe,orient=VERTICAL)
         hospital_table=ttk.Treeview(infoframe,column=("nameoftable","ref","dose","nooftablet","lot","issuedate","expdate",
                          "dailydose", "storage","nhsnumber","pname","DOB","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)

         scroll_x=ttk.Scrollbar(command=hospital_table.xview)
         scroll_y=ttk.Scrollbar(command=hospital_table.yview)

         hospital_table.heading("nameoftable",text="Name of table")
         hospital_table.heading("ref", text="reference no")
         hospital_table.heading("dose", text="Dose")
         hospital_table.heading("nooftablet", text="Name of tablet")
         hospital_table.heading("lot", text="lot")
         hospital_table.heading("issuedate", text="issue date")
         hospital_table.heading("expdate", text="Exp date")
         hospital_table.heading("dailydose", text="Daily dose")
         hospital_table.heading("storage", text="storage")
         hospital_table.heading("nhsnumber", text="NHS number")
         hospital_table.heading("pname", text="patient name")
         hospital_table.heading("DOB", text="DOB")
         hospital_table.heading("address", text="address")

         hospital_table["show"]="headings"


         hospital_table.column("nameoftable",width=100)
         hospital_table.column("ref", width=100)
         hospital_table.column("dose", width=100)
         hospital_table.column("nooftablet", width=100)
         hospital_table.column("lot", width=100)
         hospital_table.column("issuedate", width=100)
         hospital_table.column("expdate", width=100)
         hospital_table.column("dailydose", width=100)
         hospital_table.column("storage", width=100)
         hospital_table.column("nhsnumber", width=100)
         hospital_table.column("pname", width=100)
         hospital_table.column("DOB", width=100)
         hospital_table.column("address", width=100)

         hospital_table.pack(fill=BOTH, expand=1)

def login():

     if userent.get()=="" or passwordent.get()=="":
        messagebox.showerror("Error","All fields are required")
     elif userent.get()!="marina" or passwordent.get()!="password":
        messagebox.showerror("Error","invalid username/password")
     else:
        open_main=messagebox.askyesno("yesNo","Access only admin")
        if open_main>0:

            hospital()
        else:
            if not open_main:
                return


#====================================login frame=====================================================
my_frame=Frame(root,bg="light grey",relief=GROOVE)
my_frame.place(x=100,y=350,height=340,width=500)

tittle=Label(my_frame,text="login",font=("times new roman",45,"bold"),bg="light grey")
tittle.grid(row=0,column=0)

disc=Label(my_frame,text="record of patient medical health",font=("Goudy old style",25,"bold"),bg="light grey")
disc.grid(row=1,column=0)

user=Label(my_frame,text="username",font=("Goudy old style",15,"bold"),bg="light grey")
user.grid(row=2,column=0,sticky=W)

userent=Entry(my_frame,font=("Goudy old style",15,"bold"),width=30,bg="white")
userent.grid(row=3,column=0,sticky=W)

password=Label(my_frame,text="password",font=("Goudy old style",15,"bold"),bg="light grey")
password.grid(row=4,column=0,sticky=W)
passwordent=Entry(my_frame,font=("Goudy old style",15,"bold"),width=30,bg="white")
passwordent.grid(row=5,column=0,sticky=W)

#==================================================
login_btn=Button(my_frame,text="okay",font=("Goudy old style",15,"bold"),bg="white",command=login )
login_btn.grid(row=8,column=0)




mainloop()







from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("ABC hospital")
root.geometry("1090x700+0+0")
root.iconbitmap("lg.ico")
root.resizable(False, False)
my_image = ImageTk.PhotoImage(Image.open("med.jpg"))
my_label = Label(image=my_image)
image1 = Label(root, image=my_image).place(x=0, y=0, relwidth=1, relheight=1)

conn = sqlite3.connect("record.db")
c = conn.cursor()
'''
c.execute ("""CREATE TABLE record3(
            name_of_tablet text,
            refence_no text,
            dose integer,
            lot text,
            nooftablet text,
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
    if nameoftablet.get() == "" or ref.get() == 0:
        messagebox.showerror("Error", "all fields are required", parent=top)
    else:
        conn = sqlite3.connect("record.db")

        c = conn.cursor()
        c.execute(
            "INSERT INTO record3 VALUES (:name_of_tablet, :refence_no, :dose, :lot, :nooftablet,:issue_date,:exp_date,:daily_dose,:side_effect,:gender,:blood_pressure ,:storage_advice,:medication,:patient_Id,:NHS_number ,:patient_name,:dob, :address  )",
            {
                'name_of_tablet': comember.get(),
                'refence_no': txtrefenceno.get(),
                'dose': txtdose.get(),
                'lot': txtlot.get(),
                'nooftablet': txtnooftablet.get(),
                'issue_date': txtissuedate.get(),
                'exp_date': txtexpdate.get(),
                'daily_dose': textdailydose.get(),
                'side_effect': textsideeffect.get(),
                'gender': cogender.get(),
                'blood_pressure': textbloodpressure.get(),
                'storage_advice': textstorageadvice.get(),
                'medication': textmedication.get(),
                'patient_Id': textpatientid.get(),
                'NHS_number': textnhsnumber.get(),
                'patient_name': textpatientname.get(),
                'dob': textDOB.get(),
                'address': textaddress.get()
            })

        conn.commit()
        fetch_data()
        conn.close()
        messagebox.showinfo("record", "Inserted Successfully", parent=top)


# ============================================================

def exit():
    iexit = messagebox.askyesno("pharmecy management", "confirm if you want to quit", parent=top)
    if iexit > 0:
        root.destroy()
        return


def clear():
    comember.delete(0, END)
    txtrefenceno.delete(0, END)
    txtdose.delete(0, END)
    txtlot.delete(0, END)
    txtnooftablet.delete(0, END)
    txtissuedate.delete(0, END)
    txtexpdate.delete(0, END)
    textdailydose.delete(0, END)
    textsideeffect.delete(0, END)
    cogender.delete(0, END)
    textbloodpressure.delete(0, END)
    textstorageadvice.delete(0, END)
    textmedication.delete(0, END)
    textpatientid.delete(0, END)
    textnhsnumber.delete(0, END)
    textpatientid.delete(0, END)
    textDOB.delete(0, END)
    textaddress.delete(0, END)
    textpatientname.delete(0, END)


def fetch_data():
    conn = sqlite3.connect('record.db')

    c = conn.cursor()
    # delete a record
    c.execute("SELECT * from record3")
    rows = c.fetchall()
    if len(rows) != 0:
        hospital_table.delete(*hospital_table.get_children())
        for i in rows:
            hospital_table.insert("", END, values=i)

        conn.commit()
    conn.close()


def get_cursor(event=""):
    cursor_row = hospital_table.focus()
    content = hospital_table.item(cursor_row)
    row = content["values"]
    nameoftablet.set(row[0])
    ref.set(row[1])
    dose.set(row[2])
    nooftablet.set(row[3])
    lot.set(row[4])
    issuedate.set(row[5])
    expdate.set(row[6])
    dailydose.set(row[7])
    sideeffect.set(row[8])
    gender.set(row[9])
    b_p.set(row[10])
    storage.set(row[11])
    medication.set(row[12])
    pid.set(row[13])
    nhsnumber.set(row[14])
    pname.set(row[15])
    dateofbirth.set(row[16])
    address.set(row[17])


# def delete():
#
#     conn = sqlite3.connect('record.db')
#
#     c = conn.cursor()
#     # delete a record
#     c.execute("DELETE from record1 WHERE oid = " +patient_id.get())
#     print('Deleted Successfully')
#     # query of the database
#     c.execute("SELECT *, oid FROM record1")
#     records = c.fetchall()
#     # print(records)
#     # Loop through the results
#     print_record = ''
#     for record in records:
#
#         print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[2]) + str(record[3]) + ' ' + str(record[4]) + ' ' + '\t' + str(record[18]) + "\n"
#     query_label = Label(top, text=print_record)
#     query_label.place(x=500,y=500)
#     conn.commit()
#     conn.close()oid': update_id

def prescreptiondata():
    txtprescription.insert(END, "Name:\t\t" + pname.get() + "\n")
    txtprescription.insert(END, "name of Tablets:\t\t" + nameoftablet.get() + "\n")
    txtprescription.insert(END, "ref no:\t\t" + ref.get() + "\n")
    txtprescription.insert(END, "ID:\t\t" + pid.get() + "\n")
    txtprescription.insert(END, "dose:\t\t" + dose.get() + "\n")
    txtprescription.insert(END, "NO of tablets:\t\t" + nooftablet.get() + "\n")
    txtprescription.insert(END, "lot:\t\t" + lot.get() + "\n")
    txtprescription.insert(END, "Issue Date:\t\t" + issuedate.get() + "\n")
    txtprescription.insert(END, "EXP Date:\t\t" + expdate.get() + "\n")
    txtprescription.insert(END, "daily dose:\t\t" + dailydose.get() + "\n")
    txtprescription.insert(END, "side effect:\t\t" + sideeffect.get() + "\n")
    txtprescription.insert(END, "Gender:\t\t" + gender.get() + "\n")
    txtprescription.insert(END, "pressure:\t\t" + b_p.get() + "\n")
    txtprescription.insert(END, "storage:\t\t" + storage.get() + "\n")
    txtprescription.insert(END, "medication:\t\t" + medication.get() + "\n")
    txtprescription.insert(END, "DOB:\t\t" + dateofbirth.get() + "\n")
    txtprescription.insert(END, "Address:\t\t" + address.get() + "\n")


# refence_no= :ref,
def update():
    conn = sqlite3.connect('record.db')
    c = conn.cursor()
    # update a record
    update_id = txtrefenceno.get()
    c.execute(""" UPDATE record3 SET
    name_of_tablet= :tablet,
    refence_no= :ref_no,
    dose= :dose,
    lot= :lot,
    nooftablet= :numoftablet,
    issue_date= :issuedate,
    exp_date= :expdate,
    daily_dose= :dailydose,
    side_effect= :sideeffect,
    gender= :gender,
    blood_pressure= :bloodpressure,
    storage_advice= :storageadvice,
    medication= :medication,
    patient_Id= :patientid,
    NHS_number= :nhsnumber,
    patient_name= :patientname,
    dob= :DOB,
    address= :address
    WHERE oid= :oid""",
              {
                  'tablet': nameoftablet.get(),
                  'ref_no': ref.get(),
                  'dose': dose.get(),
                  'lot': lot.get(),
                  'numoftablet': nooftablet.get(),
                  'issuedate': issuedate.get(),
                  'expdate': expdate.get(),
                  'dailydose': dailydose.get(),
                  'sideeffect': sideeffect.get(),
                  'gender': gender.get(),
                  'bloodpressure': b_p.get(),
                  'storageadvice': storage.get(),
                  'medication': medication.get(),
                  'patientid': pid.get(),
                  'nhsnumber': nhsnumber.get(),
                  'patientname': pname.get(),
                  'DOB': dateofbirth.get(),
                  'address': address.get(),
                  'oid': update_id
              }
              )

    conn.commit()
    fetch_data()
    conn.close()
    messagebox.showinfo("sucess", "update data", parent=top)


def hospital():
    global my_hospital
    global top
    top = Toplevel()

    top.title(" hospital management system")
    top.geometry("1370x800+0+0")
    title = Label(top, text="Hospital management system", bd=6, relief=GROOVE, font=("times new roman", 50, "bold"),
                  bg="powder blue", fg="black")
    title.pack(side=TOP, fill=X)
    frame = Frame(top, bd=9, relief=RIDGE, padx=20, bg="powder blue").place(x=10, y=100, width=1350, height=400)
    # =======dataframeleft===========================================================
    Dataframeleft = LabelFrame(top, text="patient information", bd=6, bg="powder blue", fg="green",
                               font=("times new roman", 10, "bold"))
    Dataframeleft.place(x=30, y=130, width=700, height=350)
    # creating global

    global comember
    global txtrefenceno
    global txtdose
    global txtnooftablet
    global txtlot
    global txtissuedate
    global txtexpdate
    global textdailydose
    global textsideeffect
    global cogender
    global textbloodpressure
    global textstorageadvice
    global textmedication
    global textnhsnumber
    global textpatientid
    global textDOB
    global textaddress
    global textpatientname
    global Dataframeright
    global infoframe
    global txtprescription
    global hospital_table

    global nameoftablet
    global ref
    global dose
    global nooftablet
    global lot
    global issuedate
    global expdate
    global dailydose
    global sideeffect
    global gender
    global b_p
    global medication
    global storage
    global nhsnumber
    global pname
    global pid
    global dateofbirth
    global address

    nameoftablet = StringVar()
    ref = StringVar()
    dose = StringVar()
    nooftablet = StringVar()
    lot = StringVar()
    issuedate = StringVar()
    expdate = StringVar()
    dailydose = StringVar()
    sideeffect = StringVar()
    gender = StringVar()
    b_p = StringVar()
    medication = StringVar()
    storage = StringVar()
    nhsnumber = StringVar()
    pname = StringVar()
    pid = StringVar()
    dateofbirth = StringVar()
    address = StringVar()

    # =====creating combobox======================================================================
    lblmember = Label(Dataframeleft, text="Name of tablet", bg="powder blue", font=("arial", 15)).grid(row=0, column=0,
                                                                                                       sticky=W)
    comember = ttk.Combobox(Dataframeleft, textvariable=nameoftablet, font=("arial", 10), width=27, state="readonly")
    comember["value"] = ("covid", "antibiotic", "pills")
    comember.grid(row=0, column=1, sticky=W)
    # ====creating text column===================================================================================
    lblrefenceno = Label(Dataframeleft, text="Refence no", bg="powder blue", font=("arial", 15), padx=2, pady=3).grid(
        row=1, column=0, sticky=W)
    txtrefenceno = Entry(Dataframeleft, textvariable=ref, font=("arial", 10), width=30)
    txtrefenceno.grid(row=1, column=1, sticky=W)

    lbldose = Label(Dataframeleft, text="Dose", bg="powder blue", font=("arial", 15), padx=2,
                    pady=3).grid(row=2, column=0, sticky=W)
    txtdose = Entry(Dataframeleft, textvariable=dose, font=("arial", 10), width=30)
    txtdose.grid(row=2, column=1, sticky=W)

    lblnoftablet = Label(Dataframeleft, text="No of tablet", bg="powder blue", font=("arial", 15), padx=2,
                         pady=3).grid(row=3, column=0, sticky=W)
    txtnooftablet = Entry(Dataframeleft, textvariable=nooftablet, font=("arial", 10), width=30)
    txtnooftablet.grid(row=3, column=1, sticky=W)

    lbllot = Label(Dataframeleft, text="lot", bg="powder blue", font=("arial", 15), padx=2,
                   pady=3).grid(row=4, column=0, sticky=W)
    txtlot = Entry(Dataframeleft, textvariable=lot, font=("arial", 10), width=30)
    txtlot.grid(row=4, column=1, sticky=W)

    lblissuedate = Label(Dataframeleft, text="Issue date", bg="powder blue", font=("arial", 15), padx=2,
                         pady=3).grid(row=5, column=0, sticky=W)
    txtissuedate = Entry(Dataframeleft, textvariable=issuedate, font=("arial", 10), width=30)
    txtissuedate.grid(row=5, column=1, sticky=W)

    lblexpdate = Label(Dataframeleft, text="exp date", bg="powder blue", font=("arial", 15), padx=2,
                       pady=3).grid(row=6, column=0, sticky=W)
    txtexpdate = Entry(Dataframeleft, textvariable=expdate, font=("arial", 10), width=30)
    txtexpdate.grid(row=6, column=1, sticky=W)

    lbldailydose = Label(Dataframeleft, bg="powder blue", text="Daily dose", font=("arial", 15), padx=2, pady=3).grid(
        row=7
        , column=0, sticky=W)
    textdailydose = Entry(Dataframeleft, textvariable=dailydose, font=("arial", 10), width=30)
    textdailydose.grid(row=7, column=1, sticky=W)

    lblsideeffect = Label(Dataframeleft, bg="powder blue", text="side effect", font=("arial", 15), padx=2, pady=3).grid(
        row=8, column=0, sticky=W)
    textsideeffect = Entry(Dataframeleft, textvariable=sideeffect, font=("arial", 10), width=30)
    textsideeffect.grid(row=8, column=1, sticky=W)

    # ====creating COMBOBOX======================================================================
    lblgender = Label(Dataframeleft, text="gender", bg="powder blue", font=("arial", 15)).grid(row=0, column=3,
                                                                                               sticky=W)
    cogender = ttk.Combobox(Dataframeleft, textvariable=gender, font=("arial", 10), width=25, state="readonly")
    cogender["value"] = ("female", "male")
    cogender.grid(row=0, column=4, sticky=W)
    # ==============================================================================================

    lblbloodpressure = Label(Dataframeleft, bg="powder blue", text="Blood pressure", font=("arial", 15), padx=2,
                             pady=3).grid(
        row=1, column=3, sticky=W)
    textbloodpressure = Entry(Dataframeleft, textvariable=b_p, font=("arial", 10), width=27)
    textbloodpressure.grid(row=1, column=4, sticky=W)

    lblstorageadvice = Label(Dataframeleft, bg="powder blue", text="storage advice", font=("arial", 15), padx=2,
                             pady=3).grid(
        row=2, column=3, sticky=W)
    textstorageadvice = Entry(Dataframeleft, textvariable=storage, font=("arial", 10), width=27)
    textstorageadvice.grid(row=2, column=4, sticky=W)

    lblmedication = Label(Dataframeleft, bg="powder blue", text="Medication", font=("arial", 15), padx=2, pady=3).grid(
        row=3, column=3, sticky=W)
    textmedication = Entry(Dataframeleft, textvariable=medication, font=("arial", 10), width=27)
    textmedication.grid(row=3, column=4, sticky=W)

    lblpatientid = Label(Dataframeleft, bg="powder blue", text="patient ID", font=("arial", 15), padx=2,
                         pady=3).grid(
        row=4, column=3, sticky=W)
    textpatientid = Entry(Dataframeleft, textvariable=pid, font=("arial", 10), width=27)
    textpatientid.grid(row=4, column=4, sticky=W)

    lblnhsnumber = Label(Dataframeleft, bg="powder blue", text="NHS number", font=("arial", 15), padx=2,
                         pady=3).grid(
        row=5, column=3, sticky=W)
    textnhsnumber = Entry(Dataframeleft, textvariable=nhsnumber, font=("arial", 10), width=27)
    textnhsnumber.grid(row=5, column=4, sticky=W)

    lblpatientname = Label(Dataframeleft, bg="powder blue", text="Patient name", font=("arial", 15), padx=2,
                           pady=3).grid(
        row=6, column=3, sticky=W)
    textpatientname = Entry(Dataframeleft, textvariable=pname, font=("arial", 10), width=27)
    textpatientname.grid(row=6, column=4, sticky=W)

    lblDOB = Label(Dataframeleft, bg="powder blue", text="DOB", font=("arial", 15), padx=2,
                   pady=3).grid(
        row=7, column=3, sticky=W)
    textDOB = Entry(Dataframeleft, textvariable=dateofbirth, font=("arial", 10), width=27)
    textDOB.grid(row=7, column=4, sticky=W)

    lbladdress = Label(Dataframeleft, bg="powder blue", text="address", font=("arial", 15), padx=2,
                       pady=3).grid(
        row=8, column=3, sticky=W)
    textaddress = Entry(Dataframeleft, textvariable=address, font=("arial", 10), width=27)
    textaddress.grid(row=8, column=4, sticky=W)

    # =====dATA FRAME RIGHT=======================================================================================
    Dataframeright = LabelFrame(top, text="prescription", bd=6, bg="powder blue", fg="green",
                                font=("times new romen", 10, "bold"))
    Dataframeright.place(x=750, y=130, width=590, height=350)
    txtprescription = Text(Dataframeright, bg="white", fg="green", font=("times new romen", 10, "bold")
                           , width=80, height=19, padx=5, pady=6)

    txtprescription.grid(row=0, column=0)

    # ======button frame===========================================================================================
    buttonframe = LabelFrame(top, bd=6, bg="powder blue")
    buttonframe.place(x=10, y=505, width=1350, height=90)

    # ====================adding button============================================================================

    btnprescripton = Button(buttonframe, text="prescription", font=("arial", 12, "bold"), width=20, height=2,
                            bg="light grey", padx=4, pady=6, command=prescriton)
    btnprescripton.grid(row=0, column=0)

    btnprescriptondata = Button(buttonframe, text="prescription data", font=("arial", 12, "bold"), width=20, height=2,
                                bg="light grey", padx=4, pady=6, command=prescreptiondata)
    btnprescriptondata.grid(row=0, column=1)

    btnupdate = Button(buttonframe, text="update", font=("arial", 12, "bold"), width=20, height=2,
                       bg="light grey", padx=4, pady=6, command=update)
    btnupdate.grid(row=0, column=2)

    btndelete = Button(buttonframe, text="delete", font=("arial", 12, "bold"), width=20, height=2,
                       bg="light grey", padx=4, pady=6, )
    btndelete.grid(row=0, column=3)

    btnclear = Button(buttonframe, text="clear", font=("arial", 12, "bold"), width=20, height=2,
                      bg="light grey", padx=4, pady=6, command=clear)
    btnclear.grid(row=0, column=4)

    btnexit = Button(buttonframe, text="exit", font=("arial", 12, "bold"), width=20, height=2,
                     bg="light grey", padx=4, pady=6, command=exit)
    btnexit.grid(row=0, column=5)

    # ==============table==============================================================================

    # ====information frame================================================================================
    infoframe = LabelFrame(top, bd=6, bg="powder blue")
    infoframe.place(x=10, y=595, width=1350, height=190)

    # ======================scrollbar============================================================

    scroll_x = ttk.Scrollbar(infoframe, orient=HORIZONTAL)
    scroll_y = ttk.Scrollbar(infoframe, orient=VERTICAL)
    hospital_table = ttk.Treeview(infoframe,
                                  column=("nameoftablet", "ref", "dose", "nooftablet", "lot", "issuedate", "expdate",
                                          "dailydose", "sideeffect", "gender", "b_p", "storage", "medication", "pid",
                                          "nhsnumber", "pname", "dateofbirth", "address"),
                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set, )

    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)

    scroll_x = ttk.Scrollbar(command=hospital_table.xview)
    scroll_y = ttk.Scrollbar(command=hospital_table.yview)

    hospital_table.heading("nameoftablet", text="Name of tablet")
    hospital_table.heading("ref", text="reference no")
    hospital_table.heading("dose", text="Dose")
    hospital_table.heading("nooftablet", text="N0 of tablet")
    hospital_table.heading("lot", text="lot")
    hospital_table.heading("issuedate", text="issue date")
    hospital_table.heading("expdate", text="Exp date")
    hospital_table.heading("dailydose", text="Daily dose")
    hospital_table.heading("sideeffect", text="side effect")
    hospital_table.heading("gender", text="gender")
    hospital_table.heading("b_p", text="pressure")
    hospital_table.heading("storage", text="storage")
    hospital_table.heading("medication", text="medication")
    hospital_table.heading("pid", text="ID no")
    hospital_table.heading("nhsnumber", text="NHS number")
    hospital_table.heading("pname", text="patient name")
    hospital_table.heading("dateofbirth", text="DOB")
    hospital_table.heading("address", text="address")

    hospital_table["show"] = "headings"

    hospital_table.column("nameoftablet", width=70)
    hospital_table.column("ref", width=70)
    hospital_table.column("dose", width=70)
    hospital_table.column("nooftablet", width=70)
    hospital_table.column("lot", width=70)
    hospital_table.column("issuedate", width=70)
    hospital_table.column("expdate", width=70)
    hospital_table.column("dailydose", width=70)
    hospital_table.column("sideeffect", width=70)
    hospital_table.column("gender", width=70)
    hospital_table.column("b_p", width=70)
    hospital_table.column("storage", width=70)
    hospital_table.column("medication", width=70)
    hospital_table.column("pid", width=70)
    hospital_table.column("nhsnumber", width=70)
    hospital_table.column("pname", width=70)
    hospital_table.column("dateofbirth", width=70)
    hospital_table.column("address", width=70)

    hospital_table.pack(fill=BOTH, expand=1)

    hospital_table.bind("<ButtonRelease-1>", get_cursor)
    fetch_data()


def login():
    if userent.get() == "" or passwordent.get() == "":
        messagebox.showerror("Error", "All fields are required")
    elif userent.get() != "marina" or passwordent.get() != "password":
        messagebox.showerror("Error", "invalid username/password")
    else:
        open_main = messagebox.askyesno("yesNo", "Access only admin")
        if open_main > 0:

            app = hospital()
        else:
            if not open_main:
                return


# ====================================login frame=====================================================
my_frame = Frame(root, bg="light grey", relief=GROOVE)
my_frame.place(x=500, y=350, height=300, width=520)

tittle = Label(my_frame, text="login", font=("times new roman", 45, "bold"), bg="light grey")
tittle.grid(row=0, column=0)

disc = Label(my_frame, text="record of patient medical health", font=("Goudy old style", 25, "bold"), bg="light grey")
disc.grid(row=1, column=0)

user = Label(my_frame, text="username", font=("Goudy old style", 15, "bold"), bg="light grey")
user.grid(row=2, column=0, sticky=W)

userent = Entry(my_frame, font=("Goudy old style", 15, "bold"), width=30, bg="white")
userent.grid(row=3, column=0, sticky=W)

password = Label(my_frame, text="password", font=("Goudy old style", 15, "bold"), bg="light grey")
password.grid(row=4, column=0, sticky=W)
passwordent = Entry(my_frame, font=("Goudy old style", 15, "bold"), width=30, bg="white")
passwordent.grid(row=5, column=0, sticky=W)

# ==================================================
login_btn = Button(my_frame, text="okay", font=("Goudy old style", 15, "bold"), bg="white", command=login)
login_btn.grid(row=8, column=0)

mainloop()







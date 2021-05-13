from tkinter import *
import sqlite3

root = Tk()
root.title("database")

# database

# creating database
con = (sqlite3.connect("book.db"))

# create cursor
# cursor class is an instance using which you can invoke
# methonds that execute sqlite statements,fetch data frm the result sets of the queris
c = con.cursor()


# create table
# c.execute("""CREATE TABLE addresses(
#         name text,
#         address text,
#        city text,
#        contact integer
#  )
#  """)
# print("database ")


def submit():
    con = sqlite3.connect("book.db")

    c = con.cursor()
    # insert into table
    c.execute("INSERT INTO addresses VALUES  (:entname,:entadd,:entcity,:entcontact)", {
        'entname': entname.get(),
        'entadd': entadd.get(),
        'entcity': entcity.get(),
        'entcontact': entcontact.get()
    })
    print("address inserted successfully")

    entname.delete(0, END)
    entadd.delete(0, END)
    entcity.delete(0, END)
    entcontact.delete(0, END)


def query():
    # Create a databases or connect to one
    con = sqlite3.connect('book.db')

    # Create cursor
    c = con.cursor()

    # query of the database
    c.execute("SELECT * FROM addresses ")

    records = c.fetchall()
    print(records)

    # Loop through the results
    print_record = ''
    for record in records:
        print_record += str(record) + "\n"

    query_label = Label(root, text=print_record)
    query_label.grid(row=8, column=0, columnspan=2)

    con.commit()
    con.close()

    # #create a database
    # con = sqlite3.connect("book.db")
    #
    # c = con.cursor()
    #
    # c.execute("SELECT *, oid FROM addresses")
    #
    # records=c.fetchall()
    # print(records)
    # #loop through the result
    # print_record=""
    # for record in records:
    #     print_record +=str(record) + "\n"
    #
    # query_label=Label(root,text=print_record)
    # query_label.grid(row=7,column=0,columnspan=2)
    #
    #
    # con.commit()
    # con.close()


# ===== creting laebl and entry
lblname = Label(root, text="Name").grid(row=0, column=0)
entname = Entry(root, bd=4, width=25)
entname.grid(row=0, column=1)

lbladd = Label(root, text="Address").grid(row=1, column=0)
entadd = Entry(root, bd=4, width=25)
entadd.grid(row=1, column=1)

lblcity = Label(root, text="City").grid(row=2, column=0)
entcity = Entry(root, bd=4, width=25)
entcity.grid(row=2, column=1)

lblcontact = Label(root, text="Contact").grid(row=3, column=0)
entcontact = Entry(root, bd=4, width=25)
entcontact.grid(row=3, column=1)

btnadd = Button(root, text="Add Record", width=25, bd=4, command=submit)
btnadd.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipadx=10)

btnrecord = Button(root, text="show record", width=25, bd=4, command=query)
btnrecord.grid(row=5, column=0, columnspan=2)

lbldeleteid = Label(root, text="Name").grid(row=0, column=0)
entdeleteid = Entry(root, bd=4, width=25)
entdeleteid.grid(row=7, column=1)

# commit
con.commit()

con.close()

mainloop()
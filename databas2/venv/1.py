from tkinter import *
import sqlite3

root = Tk()
root.title("Database Address Book")

#Database


#Create a databases  or connect tp one

conn = sqlite3.connect("address_book.db")

#create cursor
'''Cursor class is an instance using which you invoke methods that executes SQLite statements, 
fetch data from the result sets of the queries'''


c = conn.cursor()


#Create table
'''
c.execute(""" CREATE TABLE addresses(
    first_name text,
    last_name text, 
    address text,
    city text,
    state text,
    zipcode integer
)
""")

print("Table created successfully")

#commit change
conn.commit()

#close connection
conn.close()
'''''

#Create submit button for datebase
def submit():
    # Create a databases or conect to one
    conn = sqlite3.connect("address_book.db")

    #create curser
    c= conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", {
        'f_name': first_name.get(),
        'l_name': last_name.get(),
        'address': address.get(),
        'city': city.get(),
        'state': state.get(),
        'zipcode': zipcode.get()
    })
    print('Address inserted successfully')

    conn.commit()
    conn.close()


    first_name.delete(0,END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


#Create submit button for datebase
def query():
    # Create a databases or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
    # query of the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)
    # Loop through the results
    print_record = ''
    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1]) + '' +'\t' + str(record[6]) + "\n"
    query_label = Label(root, text=print_record)
    query_label.grid(row=12, column=0, columnspan=2)

    conn.commit()
    conn.close()


def delete1():
    conn=sqlite3.connect('address_book.db')

    c=conn.cursor()

    c.execute("DElETE from addresses WHERE oid = " + delete.get())
    print('delete successfully')

    c.execute("SELECT *,oid FROM addresses")
    records=c.fetchall()

    print_record=""
    for record in records:
        print_record += str(record[0]) + ' '+ str(record[1]) + ' ' + '\t' + str(record[6]) + "\n"
        query_label = Label(root, text=print_record)
        query_label.grid(row=12, column=0, columnspan=2)

        conn.commit()
        conn.close()

def edit():
    global editor
    editor=Tk()
    editor.title("update data")
    editor.geometry('300x480')
#create database or  connect to one
    conn=sqlite3.connect('address_book.db')

    c=conn.cursor

    record_id= delete.get()

    c.execute("SELECT * FROM addresses WHERE oid=" + record_id)

    records=c.fetchall()

    #creating global variable for all text boxes
    global first_name_editor
    global last_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor


    # Create tet boxes
    first_name_editor = Entry(editor, width=30)
    first_name_editor.grid(row=0, column=1, padx=20)

    last_name_editor = Entry(editor, width=30)
    last_name_editor.grid(row=1, column=1)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    first_name_label = Label(root, text="First Name")
    first_name_label.grid(row=0, column=0)

    last_name_label = Label(root, text="First Name")
    last_name_label.grid(row=1, column=0)

    address_label = Label(root, text="Address")
    address_label.grid(row=2, column=0)

    city_label = Label(root, text="City")
    city_label.grid(row=3, column=0)

    state_label = Label(root, text="State")
    state_label.grid(row=4, column=0)

    zipcode_label = Label(root, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    #loop through the result
    for record in records:
        first_name_editor.insert(0, record[0])
        last_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

 #create update button
    edit_btn = Button(editor, text="save")
    edit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

def update():
    conn=sqlite3.connect("address_book.db")
    record_id=delete.get()
    c.execute(''' UPDATE adresses SET
    first_name=:first,
    last_name=:last,
    address=:address,
    city=:city,
    zipcode=:zipcode,
     oid=:oid'''),
    {'first':first_name_editor.get(),
     "last": last_name_editor.get(),
     "address":address_editor.get(),
     "state": state_editor.get(),
     "zipcode":zipcode_editor.get(),
     "oid":record_id
    }
    conn.commit()
    conn.close()
    #destroyig all the data and closing window
    editor.destroy()

#Create tet boxes
first_name = Entry(root, width=30)
first_name.grid(row=0, column=1, padx=20)

last_name = Entry(root, width=30)
last_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete= Entry(root, width=30)
delete.grid(row=8, column=1)

first_name_label = Label(root, text="First Name")
first_name_label.grid(row=0,column=0)

last_name_label = Label(root, text="First Name")
last_name_label.grid(row=1,column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2,column=0)

city_label = Label(root, text="City")
city_label.grid(row=3,column=0)

state_label = Label(root, text="State")
state_label.grid(row=4,column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_label =Label(root, text="student ID")
delete_label.grid(row=8, column=0)

#Create Submit Button

submit_btn = Button(root, text=("Submit Your Details"), command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Create Show Record Button

print_record_btn = Button(root, text=("Show Records"), command=query)
print_record_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Create Delete Button
delete_btn = Button(root, text=("Delete"), command=delete1)
delete_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#crete update button
create_btn=Button(root,text=("update"),command=edit)
create_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=100)


mainloop()
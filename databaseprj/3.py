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

'''
#Create table
c.execute(""" CREATE TABLE addresses(
    first_name text,
    last_name text, 
    address text,
    city text,
    state text,
    zipcode integer
)
""")

print("Table created successfully")'''

#commit change
conn.commit()

#close connection
conn.close()


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
        print_record += str(record[0]) + ' ' + str(record[1]) + "\n"
    query_label = Label(root, text=print_record)
    query_label.grid(row=7, column=0, columnspan=2)

    conn.commit()
    conn.close()


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

delete = Entry(root, width=30)
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

delete_label =Label(root, text="Delete ID")
delete_label.grid(row=8, column=0)

#Create Submit Button

submit_btn = Button(root, text=("Submit Your Details"), command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Create Show Record Button

print_record_btn = Button(root, text=("Show Records"), command=query)
print_record_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Create Delete Button
delete_btn = Button(root, text=("Delete"), command=delete)
delete_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

mainloop()
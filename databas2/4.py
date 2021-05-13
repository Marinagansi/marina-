from tkinter import*
import sqlite3

root=Tk()
root.title("database Address book")
# creating a database or connect to one
conn=sqlite3.connect('address_book.db')
# creating cursor
# cursor class is an instance using which you can invoke methods that
# execute SQLITE statements,fetch data from the result sets of the queries
c=conn.cursor()
# create table
#  c.execute("""CREATE TABLE addresses(
#            first_name text,
#            last_name text,
#            address text,
#            city text,
#            state text,
#            zipcode integer
# )
# """)

def submit():
# create a database or connect to one
    conn=sqlite3.connect('address_book.db')
    # create cursor
    c=conn.cursor()

    # insert into table
    c.execute("INSERT INTO addresses VALUES(:first_name,:last_name,:address,:city,:state,:zipcode)",{
        'first_name':first_name.get(),
        'last_name':last_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zipcode':zipcode.get(),
        'delete':deletebox.get()
    })
    print('address inserted successfully')

    conn.commit()

    conn.close()

    # clear the text boxes
    first_name.delete(0,END)
    last_name.delete(0,END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    deletebox.delete(0,END)
def query():
    conn=sqlite3.connect('address_book.db')

    c=conn.cursor()
    c.execute("SELECT *,oid FROM addresses")

    records=c.fetchall()
    print(records)

    print_record=''
    for record in records:
        print_record +=str(record[0])+ " "+str(record[1])+' '+'\t'+str(record[6])+ "\n"

    query_label=Label(root,text=print_record)
    query_label.grid(row=8,column=0,columnspan=2)

    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()
    c.execute("DELETE from addresses WHERE oid="+deletebox.get())
    print('Deleted successfully')

    c.execute("SELECT *,oid FROM addresses")

    records=c.fetchall()

    print_record = ''
    for record in records:
        print_record += str(record[0]) + " " + str(record[1]) + ' ' + '\t' + str(record[6]) + "\n"

    query_label = Label(root, text=print_record)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()

def save():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()
    record_id=deletebox.get()

    c.execute("""UPDATE addresses SET
        first_name=:first,
        last_name=:last,
        address=:address,
        city=:city,
        state=:state,
        zipcode=:zipcode
        WHERE oid=:oid""",
              {'first': first_name_editor.get(),
               'last': last_name_editor.get(),
               'address': address_editor.get(),
               'city':city_editor.get(),
               'state': address_editor.get(),
               'zipcode': zipcode_editor.get(),
               'oid': record_id
               }
        )
    conn.commit()
    conn.close()

    editor.destroy()
def update():
    global editor
    editor=Tk()
    editor.title('Update Data')

    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()

    record_id=deletebox.get()

    c.execute("SELECT * FROM addresses WHERE oid="+record_id)

    records = c.fetchall()
    global first_name_editor
    global last_name_editor
    global address_editor
    global zipcode_editor
    global state_editor
    global city_editor

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

    # create textbox labels
    first_name_editor_label = Label(editor, text="first name")
    first_name_editor_label.grid(row=0, column=0)

    last_name_editor_label = Label(editor, text="last name")
    last_name_editor_label.grid(row=1, column=0)

    address_editor_label = Label(editor, text="address")
    address_editor_label.grid(row=2, column=0)

    city_editor_label = Label(editor, text="city")
    city_editor_label.grid(row=3, column=0)

    state_editor_label = Label(editor, text="state")
    state_editor_label.grid(row=4, column=0)

    zipcode_editor_label = Label(editor, text="zipcode")
    zipcode_editor_label.grid(row=5, column=0)

    for record in records:
        first_name_editor.insert(0,record[0])
        last_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    edit_btn=Button(editor,text="Save",command=save)
    edit_btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=125)



# create text box
first_name=Entry(root, width=30)
first_name.grid(row=0,column=1,padx=20)

last_name=Entry(root,width=30)
last_name.grid(row=1,column=1)

address=Entry(root,width=30)
address.grid(row=2,column=1)


city=Entry(root,width=30)
city.grid(row=3,column=1)


state=Entry(root,width=30)
state.grid(row=4,column=1)

zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1)

deletebox=Entry(root,width=30)
deletebox.grid(row=9,column=1)

# create textbox labels
first_name_label=Label(root,text="first name")
first_name_label.grid(row=0,column=0)

last_name_label=Label(root,text="last name")
last_name_label.grid(row=1,column=0)

address_label=Label(root,text="address")
address_label.grid(row=2,column=0)

city_label=Label(root,text="city")
city_label.grid(row=3,column=0)

state_label=Label(root,text="state")
state_label.grid(row=4,column=0)

zipcode_label=Label(root,text="zipcode")
zipcode_label.grid(row=5,column=0)

deletebox_label=Label(root,text="select ID")
deletebox_label.grid(row=9,column=0)

# create submit button
submit_btn=Button(root,text="add records",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
display_btn=Button(root,text="show records",command=query)
display_btn.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
delete_btn=Button(root,text="delete",command=delete)
delete_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
update_btn=Button(root,text="update",command=update)
update_btn.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
print("Table created successfully")
# commit change
conn.commit()
# close connection
conn.close()
mainloop()
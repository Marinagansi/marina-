from tkinter import*
root=Tk()
#creating label width
mylabel1=Label(root, text="hello")
mylabel2=Label(root, text="welcome")
mylabel3=Label(root,text="here")
#shoving it onto screen based upon x-aix and y-axis
#thar does not move having constant position
mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1,column=2)
mylabel3.grid(row=2,column=3)
root.mainloop()
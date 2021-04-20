from tkinter import*
EAS=Tk()
EAS.title("Event_Announcement")
#creating label widget
mylabel=Label(EAS,text="tittle")
mylabel1=Label(EAS,text="categories")
mylabel.grid(row=0,column=0)
mylabel1.grid(row=0,column=4)
EAS.mainloop()
from tkinter import*
root=Tk()
#button without any function
mybutton=Button(root,text="click here")
mybutton.pack()
#state disabled button
mybutton1=Button(root,text="click me",state=DISABLED)
mybutton1.pack()
 #button x and y paddding
mybutton2=Button (root,text="click",padx=50).pack()
mybutton3=Button(root,text="here",padx=50,pady=50).pack()
root.mainloop()
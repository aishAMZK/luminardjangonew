# tkinter
from tkinter import *

root=Tk() #Tk is a class ,calls object of the class
root.title("main window")
label1=Label(root,text="user name")
label2=Label(root,text="email address")
entry1=Entry(root)
entry2=Entry(root)
label1.pack()
label2.pack()
entry1.pack()
entry2.pack()

root.mainloop()
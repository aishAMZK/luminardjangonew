from tkinter import *
root=Tk()

def click_btn():
    print("btn clicked")
ulabel=Label(root,text="username")
plabel=Label(root,text="Password")
uentry=Entry(root)
pentry=Entry(root)

btn=Button(root,text="login",command=click_btn)
ulabel.grid(row=0,column=0)
plabel.grid(row=1,column=0)

uentry.grid(row=0,column=1)
pentry.grid(row=1,column=1)
btn.grid(row=2,column=1) #or> columnspan=2
root.mainloop()



#registration prob
# select course from students groupby course having count(*)<1;
#import necessary librarities
from tkinter import *

#setting up main window
root=Tk()
root.geometry("400x300")
root.title("main")

#Function to open New (Top Level) Window
def topwin():
    #setting up Top window
    top=Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    #adding a label widget to Top window
    l2=Label(top,text="This is toplevel window")
    l2.pack()
    
    top.mainloop()

#Adding a label and button widget to root (Main) window
l=Label(root,text="This is root window")
btn=Button(root,text="Click here to open another window",
command=topwin)

#arranging widgets
l.pack()
btn.pack()
root.mainloop()
from tkinter import *
root=Tk()
input=Entry(root,width="100")
input.grid(row=0,column=0,colspan=3)
def click():
    return
b1=Button(root,text="1",padx=50,pady=25,command=click)
b2=Button(root,text="2",padx=50,pady=25,command=click)
b3=Button(root,text="3",padx=50,pady=25,command=click)
b4=Button(root,text="4",padx=50,pady=25,command=click)
b5=Button(root,text="5",padx=50,pady=25,command=click)
b6=Button(root,text="6",padx=50,pady=25,command=click)
b7=Button(root,text="7",padx=50,pady=25,command=click)
b8=Button(root,text="8",padx=50,pady=25,command=click)
b92=Button(root,text="92",padx=50,pady=25,command=click)
root.mainloop()
from tkinter import *
from tkinter import messagebox
import MySQLdb as sql
def connection(user,passw):
    host='localhost'
    user='root'
    pw=''
    port='3306'
    db='db'
    conn=sql.connect(host=host,user=user,password=pw,port=port,db=db)
    query="Select  id from login1 where username=%s and password=%s"
    val=(user,passw)
    cur=conn.cursor()
    cur.execute(query,val)
    res=cur.fetchal()
    return res
    conn.close()
def check():
    u_name=un.get()

    pass_word=pw.get()
    data=connection(u_name,pass_word)
    if len(data)>0:
        messagebox.showinfo(title="hekko World!",message="Welome Login Successful")
    else:
        messagebox.showinfo(title="Hello User",message="Please Enter Correct credential")
root=Tk()
root.geometry("300x250")
root.title("Chokkalingam")
t=Label(root,text="Login Form",font=('arial',14), bd=15)
t.pack()
un=StringVar()
pw=StringVar()
form=Frame(root)
form.pack(side = TOP ,fill=X)
nameL=Label(form,text="User Name:",font=('arial',14),bd=15)
passL=Label(form,text="PasswordL",font=('arial',14),bd=15)
nameL.grid(row=1,sticky=W)
passL.grid(row=2,sticky=W)
nameE=Entry(form,textvariable=un)
passE=Entry(form,textvariable=pw,show="*")
nameE.grid(row=1,column=2)
passE.grid(row=2,column=2)
login=Button(root,text="Login",command=check)
login.pack()
root.mainloop()
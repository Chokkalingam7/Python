import mysql.connector;
con=mysql.connector.connect(host="127.0.0.1",user="root",password="",database="db1")
a=int(input("""Enter details for 1.Doctor
            2.PAtient
            3.Co-Worker"""))
if(a==1):
    def insert(name,ex,spec):
     res=con.cursor()
     sql="insert into doc(name,ex,specs)values(%s,%s,%s)"
     st=(name,ex,specs)
     res.execute(sql,st)
     con.commit()
     print(name,"Data Insert  Success")
    def update(name,ex,specs,id):
     res=con.cursor()
     sql="update doc set name=%s,ex=%s,specs=%s where id=%s"
     st=(name,ex,specs,id)
     res.execute(sql,st)
     con.commit()
     print(id,"Data Updated")
    def select():
     res=con.cursor()
     sql="select *from doc"
     res.execute(sql)
     result=res.fetchall()
     print(result)
    def delete(name):
     res=con.cursor()
     sql="delete from doc where name=%s"
     st=(name,)
     res.execute(sql,st)
     con.commit()
     print(id,"DAta Deleted")
    while True:
     print("""
        1.Insert a Data
        2.Update a Data
        3.Select a Data
        4.Delte a Data
        5.Exit""")
     ch=int(input("Enter your choice  "))
     if(ch==1):
        name=input("Enter Doctor Name  ")
        ex=int(input("Enter experience of the Doctor  "))
        specs=input("Enter Specialization of the doctor  ")
        insert(name,ex,specs)
     elif(ch==2):
        id=int(input("Enter the id of the Doctor need to Updated: "))
        name=input("Enter name of te Doctor need to Updated: ")
        ex=int(input("Enter the Experience of the Doctor need to Updated: "))
        specs=input("Enter Specialization of Doctor need to Updated  ")
        update(name,ex,specs,id)

     elif(ch==3):
        select()
     elif(ch==4):
        name=input("Enter the name of Doctor ")
        delete(name)
     elif(ch==5):
       quit()
     else:
        print("Inavlid Selection")
        print("Please Try Again")
if(a==2):
    def insert(name,age,dept):
     res=con.cursor()
     sql="insert into pat(name,age,dept)values(%s,%s,%s)"
     st=(name,age,dept)
     res.execute(sql,st)
     con.commit()
     print("Data Insert  Success")
    def select():
     res=con.cursor()
     sql="select *from pat"
     res.execute(sql)
     result=res.fetchall()
     print(result)
    def update(name,age,dept,id):
     res=con.cursor()
     sql="update pat set name=%s,age=%s,dept=%s where id=%s"
     st=(name,age,dept,id)
     res.execute(sql,st)
     con.commit()
     print(id,"Data Updated")
    def delete(name):
     res=con.cursor()
     sql="delete from pat where name=%s"
     st=(name,)
     res.execute(sql,st)
     con.commit()
     print("DAta Deleted")
    while True:
     print("1.Insert a DAta")
     print("2.Select a Data")
     print("3.Delte a Data")
     print("4.Exit")
     ch=int(input("Enter your choice  "))
     if(ch==1):
        name=input("Enter Patient Name  ")
        age=int(input("Enter Age of the PAtient  "))
        dept=input("Enter Department they looking for Treatment  ")
        insert(name,age,dept)
     elif(ch==2):
        id=int(input("Enter the id of the Doctor need to Updated: "))
        name=input("Enter name of te Doctor need to Updated: ")
        age=int(input("Enter the Age of PAtient need to Updated: "))
        dept=input("Enter DEpartment  need to Updated  ")
        update(name,age,dept,id)
     elif(ch==2):
        select()

     elif(ch==3):
        name=input("Enter the name of Patient ")
        delete(name)
     elif(ch==4):
       quit()
     else:
        print("Invalid Selection")
        print("Please Try Again")
if(a==3):
    def insert(name,pos,qual):
     res=con.cursor()
     sql="insert into co(name,pos,qual)values(%s,%s,%s)"
     st=(name,pos,qual)
     res.execute(sql,st)
     con.commit()
     print("Data Insert  Success")
    def update(name,pos,qual,id):
     res=con.cursor()
     sql="update co set name=%s,pos=%s,qual=%s where id=%s"
     st=(name,pos,qual,id)
     res.execute(sql,st)
     con.commit()
     print(id,"Data Updated")

    def select():
     res=con.cursor()
     sql="select *from co"
     res.execute(sql)
     result=res.fetchall()
     print(result)
    def delete(name):
     res=con.cursor()
     sql="delete from co where name=%s"
     st=(name,)
     res.execute(sql,st)
     con.commit()
     print("DAta Deleted")
    while True:
     print("1.Insert a DAta")
     print("2.Select a Data")
     print("3.Delte a Data")
     print("4.Exit")
     ch=int(input("Enter your choice  "))
     if(ch==1):
        name=input("Enter Co Worker Name  ")
        pos=input("Enter Position of Co Worker  ")
        qual=input("Enter Qualification of the Co Worker  ")
        insert(name,pos,qual)
     elif(ch==2):
        id=int(input("Enter the id of the Co Worker need to Updated: "))
        name=input("Enter name of Co Worker need to Updated: ")
        pos=int(input("Enter the Position of Co worker need to Updated: "))
        qual=input("Enter Qualification of Co Worker need to Updated  ")
        update(name,pos,qual,id)
     elif(ch==2):
        select()
     elif(ch==3):
        name=input("Enter the name of Co Workers ")
        delete(name)
     elif(ch==4):
       quit()
     else:
        print("Invalid Selection")
        print("Please Try Again")

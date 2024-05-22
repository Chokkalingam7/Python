import datetime
ua=int(input("Enter aadhar number:"))
name="Chokkalingam"
address=" 5/38,New Street"
mob=9652166109
uan=1
dob=18/7/2003
if(ua==uan):
    print('''
          1.Update
          2.Download
          3.Link with bank account
          4.Link with mobile number
          ''')
    o=int(input("Enter YOur Option:"))
    if(o==1):
        print("What changes changes you want to update:")
        print('''
              1.change Name 
              2.Change Mobile number
              3.change Date of Birth
              4.change Address
              ''')
        op=int(input("Enter Your Option"))
        if(op==1):
            print("DO want to change your name in Aadhar:")
            print("Enter YOur Aadhar")
            ua=int(input("Enter Aadhar number:"))
            if(ua==uan):
                
                name=str(input("Enter Your New name:"))
                print("Your",name,"is Successfully Updated")
            else:
                print("YOur Aadhar number is incorrect!")
        if(op==2):
            print("DO You Want to chnge your mobile number")
            print("Enter Your Aadhar number:")
            ua=int(input("Enter Your Aadhar Number:"))
            if(ua==uan):
                mob=int(input("Enter Your New Mobile Number:"))
                print("Your",mob,"mobile number is Successfully Updated")
            else:
                print("YOur Aadhar number is incorrect!")
            
        if(op==3):
            print("Do YOu Want to change Date of Birth")
            print("Enter your aadhar number")
            if(ua==uan):
             dob=input("Enter Your Date of Birth")
             dob=datetime.datetime.strptime("dob,%d %m %y").date()
             
             print("Your ",dob," date of birth is Successfully Updated")    
            else:
                print("Your",dob,"Is Date of birth is Successfully Updated")
        if(op==4):
            print("Do YOu want to change the address")
            print("Enter  your aadhar number")
            if(ua==uan):
                address=str(input("Enter Yuor New Address:"))
                print("Your",address,"Address is Successfully Updated")  
            else:
                print("YOur Aadhar number is incorrect!")
    if(o==2):
        if(ua==uan):
                print("Do you want to download the Aadhar")
        else:
                print("YOur Aadhar number is incorrect!")
    if(o==3):
        print("Do you want to link the bank account") 
        if(ua==uan):
            ban=int(input("Enter your bank account number"))
            ifs=int(input("Enter IFSC Code"))
            cif=int(input("Enter your CIF Number"))
            if(ua.name==ban.name):
                print("Your Aadhar is",ban,"Bank account is Succesfully linked") 
    if(o==4):
        print("Do You Want TO Link mobile number:") 
        if(ua==uan):
            mob=int(input("Enter Your Mobile Number:"))
else:
                print("YOur Aadhar number is incorrect!")
                                            

"""for i in range(6,0,-1):
    for j in range(i):
        print("*",end=" ");
    print()
a=int(input("Enter no.o f values "))
b=0
c=1
for i in range(a+1):
    print(b)
    d=b+c
    b=c
    c=d
n=int(input("Enter a value "))
rn=sn=count=0
while(n>0):
    rn=rn*10+n%10;
    sn=sn+n%10
    count=count+1
    n=n//10
print("The reverse number ",rn)
print("The Sum of digit is ",sn)
print("The count in the number ",count)
for i in range(7):
    for j in range(1,i):
        print(j,end=" ")
    print(" ")
for i in range(7,0,-1):
    for j in range(1,i):
        print(j,end=" ")
    print("")
for i in range(6,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("")
for i in range(1,7):
    for j in range(i,7):
        print(j,end=" ")
    print(" ")
for i in range(0,6):
    for j in range(6,i,-1):
        print(j,end=" ")
    print()
for i in range(1,7):
    for j in range(1,i):
        if(j%2==0):
            print("*",end=" ")
        else:
            print(j,end=" ")
    print()
for i in range(7):
    for j in range(0,i):
        print(i,end=" ")
    print()
a=1
for i in range(7):
    for j in range(i):
        print(a,end=" ")
        a=a+1
    print()
    """
for i in range(1,6):
    for j in range(1,6-i):
        print("*",end=" ")
    for k in range(1,i):
        print(k,end=" ")
    print(" ")

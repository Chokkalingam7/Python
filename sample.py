n=int(input("Enter number of inputs"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    for k in range(2*n-i):
        print(" ",end=" ")
    for l in range(n-i,1,-1):
        print(i,end=" ")
    print()
while(True):
    n=input("What is your name? ")
    a=int(input("What is your Bidding Amount? "))
    am={n:a}
    b=input("Do you have another bidding amount(y/n)?")
    if(b=="n"):
        c=max(am,key= lambda x:am[x])
        print("THe Winner of Bidding is and amount is ",c)
        exit()
    elif(b=='y'):
        pass
    else:
        print("You Entered Mismatched word ")
        exit()
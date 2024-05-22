import math
import random
a=int(input("Enter a number "))
c=0
for i in range(2,a):
        if(a%i==0):
            c+=1
if(c==1):
    print("Prime number")
else:
    print("Not Prime Number ")
a=int(input("Enter Lower Bound  "))
b=int(input("Enter Upper Bound  "))
x=random.randint(a,b)
print("\n You have only ",round(math.log(b-a+1,2)),"chances  to guess number ")
count=0
while count<math.log(b-a+1,2):
    count+=1
    guess =int(input("Guess the number "))
    if(x==guess):
        print("congrats you did it in ",count,"try")
        break
    elif(x>guess):
        print("You guessed number small")
    elif(x<guess):
        print("Your guessed number is high")
if(count>=math.log(b-a+1,2)):
    print("Sorry! The number is ",x)
#This is Guessing Word

name=input("What is your Name?  ")
print("Good Luck! ",name)
words=['rainbow','computer','science','programming','python','mathematics','player','condition','reverse','water','board','geeks']
word=random.choice(words)
print("Guess The Character ")
guesses=''
turns=10
while turns>0:
    for char in word:
        failed=0
        if char in guesses:
            print(char)
        else:
            print("_")
            failed+=1
    if failed ==0:
        print(name,'You Win')
        print('The Word is :',word)
        break
    print()
    guess =input("Guess a Character: ")
    guesses +=guess
    if guess not in word:
        turns-=1
        print('Wrong ')
        print("YOu have ",turns)
        if turns==0:
            print("Loss in Game")
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

def ins(arr):
    for i in range(len(arr)):
        a=arr[i]
        j=i-1
        while j>=0 and a<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]=a
arr=[1,2,34,5,24,6,56,545]
ins(arr)
print(arr)
def se(arr):
    n=len(arr)
    for i in range(n):
        mi=i
        for j in range(i+1,n):
            if(arr[j]<arr[mi]):
                mi=j
                arr[i],arr[mi]=arr[mi],arr[i]
arr=[1,23,56,7,3,578,78,3456]
print("Before sorting  ",arr)
se(arr)
print('After Sorting =',arr)
def bub(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[1,23,4,5,46,9,2,3,45,8,56]
print("Before sorting  ",arr)
print('After Sorting =',arr)
import random
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
def bi(arr,l,h,a):
    if h>=l:
        m=(l+h)//2
        if arr[m]==a:
            return m
        elif arr[m]<a:
            bi(arr,m+1,h,a)
        else:
            bi(arr,l,m-1,a)
    print(l)
    print(h)
    return -1
arr=[1,2,3,4,5,6]
a=7
r=bi(arr,0,len(arr)-1,a)
if r!=-1:
     print("Elemnt Present  in array ",str(r))
else:
        print("Elemnt Present  in array ",str(r))
for i in range(6):
    print(arr[i])
print(a)

a=[1,2,3,4,5,6,7,8,9,9]
b=int(input())
c=0
for i in range(len(a)):
    if(a[i]==b):
        c+=1
        j=i
    else:
        continue
if c==1:
    print("Element present in the array",j)
else:
    print("Element not found")

a=int(input("Enter a number "))
c=0
for i in range(2,a):
        if(a%i==0):
            c+=1
if(c==1):
    print("Prime number")
else:
    print("Not Prime Number ")

a=int(input("Enter Lower Limit"))
b=int(input("Enter Upper Limit"))
print("Prime Numbers between ",a,"and ",b)
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)
a=int(input("Enter "))
c=0
while(a>0):
    b=a%10
    c=c*10+b
    a=a//10
print(c)
a=input()
b=0
c=0
d=0
for i in a:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='O' or i=='I' or i=='U'):
        b+=1
    elif(i==' ' or i=='!' or i=='#' or i=='@' or i=='$' or i=='%' or i=='^' or i=='&' or i=='*' or i==')' or i=='('):
        c+=1
    else:
        d+=1
print("No. of VOwels are ",b)
print("No. of consonants in a string",d)
print("Symbols are ",c)
a=input()
if(a==a[::-1]):
    print(a," is a palindrome")
else:
    print("NOt Palindrome")
a=input()
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print("Count no. of letters is ",str(b))

from collections import Counter
a=input("Enter String ")
b=Counter(a)
print("Letter COunt is ",b)
a=input()
b={}
for keys in a:
    b[keys]=b.get(keys,0)+1
print("Count is ",str(b))
a=int(input("Enter Value :"))
i=1
while(i<=a):
    print()
    j=1
    while(j<=i):
        print(j,end=" ")
        j+=1
    s=1
    while(s<=(a-i)*2):
        print("*",end=" ")
        s+=1
    c=i
    while(c>=1):
        print(c,end=" ")
        c-=1
    i+=1
a=int(input("enter "))
i=1
while(i<=a):
    print()
    j=1
    while(j<=i):
        if(i%2==0):
            print(i,end=" ")
        else:
            print(j,end=" ")
        j+=1
    i+=1
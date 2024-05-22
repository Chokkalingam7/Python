import random
name=input("What is your Name?  ")
print("Have a Great Day! ",name)
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
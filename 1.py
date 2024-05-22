from tkinter import *
from tkinter import messagebox
player1='X'
stop_game=False
def clicked(r,c):
    global player1
    if player1 == "X" and states[r] ==0 and stop_game==False:
        b[r].configure(text ="X")
        states[r]="X"
        player1='O'
    if player1 =='O' and states[r]==0 and stop_game==False:
        b[r].configure(text ='O')
        states[r]="O"
        player1="X"
        check_if_win()
def check_if_win():
    global stop_game
    for i in range(3):
        if states[i][0] ==states[i][1] ==states[i][2] !=0:
            stop_game=True
            winner=messagebox.showinfo("Winner is ",states[i][0] +"Won ")
            break
        elif states[0][i] ==states[1][i] ==states[2][i] !=0:
            stop_game=True
            winner=messagebox.showinfo("Winner is ",states[0][i] +"Won ")
            break
        elif states[0][0] ==states[1][1] ==states[2][2] !=0:
            stop_game=True
            winner=messagebox.showinfo("Winner is ",states[0][0] +"Won ")
            break
        elif states[0][2] ==states[1][1] ==states[2][0] !=0:
            stop_game=True
            winner=messagebox.showinfo("Winner is ",states[0][2] +"Won ")
            break
        elif states[0][0] and states[0][1] and states[0][2] !=0:
            stop_game=True
            winner=messagebox.showinfo("tie","Tie ")
            break
root=Tk()
root.title("Tic Tac Toe Game")
root.resizable(0,0)
b=[
    [0,0,0],
    [0,0,0],
    [0,0,0]]
states=[
    [0,0,0],
    [0,0,0],
    [0,0,0]]
for i in range(3):
    for j in range(3):
        b[i][j]=Button(height=4, width=8,font=('Helvetica',"20"),
                       command=lambda r=i,c=j :clicked(r,c))
        b[i][j].grid(row=i,column=j)
mainloop()


from tkinter import *
from tkinter.messagebox import showinfo
from itertools import permutations

x=2
y=""
player1=[]
player2=[]

def define_sign(num):
    global x,y
    global player1,player2
    
    #Sets of possible combinations for winning
    set1=permutations([1,2,3])
    set2=permutations([4,5,6])
    set3=permutations([7,8,9])
    set4=permutations([1,4,7])
    set5=permutations([2,5,8])
    set6=permutations([3,6,9])
    set7=permutations([1,5,9])
    set8=permutations([3,5,7])
    
    #To check if players entered any possible winning combination
    for i in set1,set2,set3,set4,set5,set6,set7,set8:
        for j in list(i):
            player1won=all(elem in player1 for elem in j)
            player2won=all(elem in player2 for elem in j)
            if player1won==True:
                showinfo("game result","Player 1 has won!")
                break
            elif player2won==True:
                showinfo("game result","Player 2 has won!")
                break
            else:
                pass
        if len(player1)==5:
            showinfo("game result","It's a draw!")
            break
            
    if num==1:
        if x%2==0: #Checks for even number, which means player 1 is playing
            y="X"
            player1.append(num)
            color="blue"
            print(player1)
        else:      #Checks for odd number, which means player 2 is playing   
            y="O"
            player2.append(num)
            color="red"
            print(player2)

        b1.config(text=y,fg=color)
        x+=1

    elif num==2:
        if x%2==0: #Checks for even number, which means player 1 is playing
            y="X"
            player1.append(num)
            color="blue"
            print(player1)
        else:      #Checks for odd number, which means player 2 is playing   
            y="O"
            player2.append(num)
            color="red"
            print(player2)

        b2.config(text=y,fg=color)
        x+=1

    elif num==3:
        if x%2==0: #Checks for even number, which means player 1 is playing
            y="X"
            player1.append(num)
            color="blue"
            print(player1)
        else:      #Checks for odd number, which means player 2 is playing   
            y="O"
            player2.append(num)
            color="red"
            print(player2)

        b3.config(text=y,fg=color)
        x+=1

    elif num==4:
        if x%2==0: #Checks for even number, which means player 1 is playing
            y="X"
            player1.append(num)
            color="blue"
            print(player1)
        else:      #Checks for odd number, which means player 2 is playing   
            y="O"
            player2.append(num)
            color="red"
            print(player2)

        b4.config(text=y,fg=color)
        x+=1

    elif num==5:
        if x%2==0: #Checks for even number, which means player 1 is playing
            y="X"
            player1.append(num)
            color="blue"
            print(player1)
        else:      #Checks for odd number, which means player 2 is playing   
            y="O"
            player2.append(num)
            color="red"
            print(player2)

        b5.config(text=y,fg=color)
        x+=1

    elif num==6:
        if x%2==0: #Checks for even number, which means player 1 is playing
            y="X"
            player1.append(num)
            color="blue"
            print(player1)
        else:      #Checks for odd number, which means player 2 is playing   
            y="O"
            player2.append(num)
            color="red"
            print(player2)

        b6.config(text=y,fg=color)
        x+=1

    elif num==7:
        if x%2==0: #Checks for even number, which means player 1 is playing
            y="X"
            player1.append(num)
            color="blue"
            print(player1)
        else:      #Checks for odd number, which means player 2 is playing   
            y="O"
            player2.append(num)
            color="red"
            print(player2)

        b7.config(text=y,fg=color)
        x+=1

    elif num==8:
        if x%2==0: #Checks for even number, which means player 1 is playing
            y="X"
            player1.append(num)
            color="blue"
            print(player1)
        else:      #Checks for odd number, which means player 2 is playing   
            y="O"
            player2.append(num)
            color="red"
            print(player2)

        b8.config(text=y,fg=color)
        x+=1

    elif num==9:
        if x%2==0: #Checks for even number, which means player 1 is playing
            y="X"
            player1.append(num)
            color="blue"
            print(player1)
        else:      #Checks for odd number, which means player 2 is playing   
            y="O"
            player2.append(num)
            color="red"
            print(player2)

        b9.config(text=y,fg=color)
        x+=1


#Labels

root=Tk()
root.title("Tic-Tac-Toe")
    

l1=Label(root,text="Tic-Tac-Toe", font=("times 15",20))
l1.grid(row=0,column=2)

l2=Label(root,text="Player 1: X", font = "times 15",fg="blue")
l2.grid(row=1,column=1)

l3=Label(root,text="Player 2: O", font = "times 15",fg="red")
l3.grid(row=1,column=3)    


#Buttons


b1=Button(root,width=20,height=10,command=lambda: define_sign(1))
b1.grid(row=2,column=1)

b2=Button(root,width=20,height=10,command=lambda: define_sign(2))
b2.grid(row=2,column=2)

b3=Button(root,width=20,height=10,command=lambda: define_sign(3))
b3.grid(row=2,column=3)

b4=Button(root,width=20,height=10,command=lambda: define_sign(4))
b4.grid(row=3,column=1)

b5=Button(root,width=20,height=10,command=lambda: define_sign(5))
b5.grid(row=3,column=2)

b6=Button(root,width=20,height=10,command=lambda: define_sign(6))
b6.grid(row=3,column=3)

b7=Button(root,width=20,height=10,command=lambda: define_sign(7))
b7.grid(row=4,column=1)

b8=Button(root,width=20,height=10,command=lambda: define_sign(8))
b8.grid(row=4,column=2)

b9=Button(root,width=20,height=10,command=lambda: define_sign(9))
b9.grid(row=4,column=3)


root.mainloop()


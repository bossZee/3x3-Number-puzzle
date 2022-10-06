from tkinter import*
import random
import time


root=Tk()
root.geometry("1150x700+0+0")
root.title("9-Puzzle")
root.configure(bg='blue')

###############################################################################################

#####  Frames  ################################################################################

rootFrame=Frame(root, bg='blue', pady=2, padx=40, width=1350,
                height=100, relief= "solid")
rootFrame.grid(row=0, column=0)

title= Label(rootFrame, font=('arial',80,'bold'), text="9-Puzzle", bd=10,
             bg='blue', fg='cyan', justify=CENTER, borderwidth=12, relief="ridge", 
             width=16)
title.grid(row=0, column=0)

mainFrame=Frame(root, bg='blue', bd=10, width=1350, height=600, relief= "ridge")
mainFrame.grid(row=1, column=0, padx=10)

buttonFrame=LabelFrame(mainFrame, text="Puzzle", font=('arial',14,'bold'),
                       bg='blue', fg='cyan', bd=10, width=525, height=500,
                       relief= "ridge")
buttonFrame.pack(side=LEFT)

scoreFrame=LabelFrame(mainFrame, font=('arial',14,'bold'), bg='blue', fg='cyan', bd=10, padx=1,
                      width=540, height=500, relief= "ridge")
scoreFrame.pack(side=RIGHT)

moveCountFrame=LabelFrame(scoreFrame, bd=10, padx=10, pady=2, width=540, height=190,
                       relief= "ridge", bg='blue')
moveCountFrame.grid(row=0,column=0)

winFrame=LabelFrame(scoreFrame, bd=10, padx=10, pady=2, width=540, height=140,
                       relief= "ridge", bg='blue')
winFrame.grid(row=1,column=0)

resetFrame=LabelFrame(scoreFrame, bd=10, padx=10, pady=2, width=540, height=140,
                       relief= "ridge", bg='blue')
resetFrame.grid(row=2,column=0)

###############################################################################################

moveCounter=0
displayMove= StringVar()
displayMove.set("Number of moves"+"\n"+"0")


gameStateString=StringVar()


def updateCounter():
    global moveCounter, displayMove
    displayMove.set("Number of moves"+"\n"+str(moveCounter))

def gameStateUpdate(gameState):
    global gameStateString
    gameStateString.set(gameState)


class Button_:
    def __init__(self, text_, x, y):
        self.enterValue = text_
        self.txtIntake= StringVar()
        self.txtIntake.set(text_)
        self.x=x
        self.y=y
        self.btnNumber= Button(buttonFrame, textvariable=self.txtIntake, 
                               font=('ariel',80), bd=5, borderwidth=4, relief="solid",
                               command=lambda i=self.x, j=self.y : emptySpotChecker(i,j))
        self.btnNumber.place(x=self.x*168, y=self.y*152, width=170, height=160)


btnCheckers=[]
name=0


for y in range(3):
    btnCheckers_=[]
    for x in range(3):
        name+=1
        if name==9:
            name="" # 9th button will be an 'empty space'
        btnCheckers_.append(Button_(str(name), x, y))
    btnCheckers.append(btnCheckers_)


def shuffle():
    global btnCheckers, moveCounter
    nums=[]
    for x in range(9):
        x+=1
        if x==9:
            nums.append("")
        else:
            nums.append(str(x))
    for y in range(len(btnCheckers)):
        for x in range(len(btnCheckers[y])):
            num= random.choice(nums)
            btnCheckers[y][x].txtIntake.set(num)
            nums.remove(num)
    moveCounter=0
    updateCounter()
    gameStateUpdate("")


lblCountMoves=Label(moveCountFrame, textvariable=displayMove, borderwidth=4, relief="ridge",
                    font=("Ariel", 40)).place(x=0, y=0, width=500, height=165)

lblWin=Label(winFrame, textvariable=gameStateString, borderwidth=4, relief="ridge",
                    font=("Ariel", 40)).place(x=0, y=0, width=500, height=115)

btnReset=Button(resetFrame, text="Reset", font=("Arial", 40, 'bold'), bd=5, borderwidth=4,
                relief="ridge", command= shuffle).place(x=0, y=0, width=500, height= 100)


shuffle() 


def emptySpotChecker(y,x):
    global btnCheckers, moveCounter
    
    if not btnCheckers[x][y].txtIntake.get()=="":
        for i in range(-1,2):
            newX=x+i
            if not(newX<0 or len(btnCheckers)-1<newX or i==0):
                if btnCheckers[newX][y].txtIntake.get()== "":
                    text= btnCheckers[x][y].txtIntake.get()
                    btnCheckers[x][y].txtIntake.set(btnCheckers[newX][y].txtIntake.get())
                    btnCheckers[newX][y].txtIntake.set(text)
                    checkWinner()
                    break
        for j in range (-1,2):
            newY=y+j
            if not(newY<0 or len(btnCheckers)-1<newY or j==0):
                if btnCheckers[x][newY].txtIntake.get()== "":
                    text= btnCheckers[x][y].txtIntake.get()
                    btnCheckers[x][y].txtIntake.set(btnCheckers[x][newY].txtIntake.get())
                    btnCheckers[x][newY].txtIntake.set(text)
                    checkWinner()
                    break
        moveCounter+=1
        updateCounter()


timeLimit=60000
startTime= time.time()


def checkWinner():
    lost=False
    for y in range(len(btnCheckers)):
        for x in range(len(btnCheckers[y])):
            if btnCheckers[y][x].enterValue != btnCheckers[y][x].txtIntake.get():
                lost=True
                break
            timePlayed= time.time()-startTime
    if not lost:
        gameStateUpdate("YOU WIN!!\nTotal time: "+str(round(timePlayed,2))+"s")
        timePlayed= time.time()-startTime
        

root.mainloop()


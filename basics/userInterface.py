'''
Created on Feb 23, 2018

@author: Monica
'''

from tkinter import Canvas,Frame,Button,BOTH,TOP,Tk, StringVar,\
    OptionMenu, Label
from tkinter.constants import  RIGHT, LEFT
from sudokuGame.sudokuGame import sudokuGame
import time
from stopwatch.stopwatch import stopwatch


MARGIN=25   #pixels around the board
SIDE=60   #width of every board cell
WIDTH=HEIGHT=MARGIN*2+SIDE*9   #the width and height for the whole board

class sudokuUi(Frame):
    '''
    initializes the Sudoku game with a board,and a level and of 
    course with the master for tkinter
    '''
    def __init__(self,parent,game,level):
        self.__game = game
        Frame.__init__(self,parent)
        self.__parent = parent
        self.row,self.col=-1,-1   #the line and column when the cursor will be 
        self.level=level
        self.__initUI()
        
        
    def __initUI(self):
        self.__parent.title("SUDOKU")
        self.timer=stopwatch(self.__parent)
        self.timer.start_stopwatch()
        self.pack(fill=BOTH)
        
        self.canvas=Canvas(self,width=WIDTH,height=HEIGHT)
        self.canvas.pack(fill=BOTH,side=TOP)
        
        
        Button(self.__parent,text="New game",command=self.new_game).pack(side=LEFT,fill=BOTH,padx=1,pady=2,expand=1)
        Button(self.__parent,text="Check",command=self.check).pack(side=RIGHT,fill=BOTH,padx=1,pady=2,expand=1)
        Button(self.__parent,text="Level",command=self.change_level).pack(side=RIGHT,fill=BOTH,padx=1,pady=2,expand=1)
       
       
        self.draw_grid()
        self.draw_puzzle()
        self.canvas.bind("<Button-1>",self.cell_clicked)
        self.canvas.bind("<Key>",self.key_pressed)

  
    def draw_grid(self):
        '''
        draw a grid divided with black lines into 3x3 squares
        '''
        for i in range(10):
            color="black" if i%3==0 else "gray"
            
            x0=MARGIN+i*SIDE
            y0=MARGIN
            x1=MARGIN+i*SIDE
            y1=HEIGHT-MARGIN
            self.canvas.create_line(x0,y0,x1,y1,fill=color)
            
            y0=MARGIN+i*SIDE
            x0=MARGIN
            y1=MARGIN+i*SIDE
            x1=WIDTH-MARGIN
            self.canvas.create_line(x0,y0,x1,y1,fill=color)
            
    def draw_puzzle(self):
        '''
        draw the puzzle
        '''
        self.canvas.delete("numbers")
        for i in range(9):
            for ii in range(9):
                answer=self.__game.start_puzzle[i][ii]
                if answer!=0:
                    x=MARGIN+ii*SIDE+SIDE/2
                    y=MARGIN+i*SIDE+SIDE/2
                    original=self.__game.puzzle[i][ii]
                    color="black" if answer==original else "green"
                    self.canvas.create_text(x,y,text=answer,tags="numbers",fill=color)
            
   
    def new_game(self):
        self.__parent.destroy()
        self.new=sudokuGame(self.level)
        self.new.start()
        
        root=Tk()
        sudokuUi(root,self.new,self.level)
        
  
    def check(self):
        '''
        check if the value,where the cursor is,is the correct one or not
        if it is will be colored with black else with red
        '''
        if self.row!=-1 and self.col!=-1:
            answer=self.__game.start_puzzle[self.row][self.col]
            correct=self.__game.solved_puzzle[self.row][self.col]
            x=MARGIN+self.col*SIDE+SIDE/2
            y=MARGIN+self.row*SIDE+SIDE/2
            if self.__game.start_puzzle[self.row][self.col]!=0:
                color="black" if answer==correct else "red"
                self.canvas.create_text(x,y,text=answer,tags="numbers",fill=color)
    
    def change_level(self):
        '''
        change the level 
        should press the button confirm to change the level and start a game in that level
        '''
        level= ("beginner","intermediate","advanced")
        self.choices=StringVar(self.__parent)
        self.choices.set(self.level)
        options=OptionMenu(self,self.choices,*level,command=self.confirm)
        options.pack()
        
    def confirm(self,ceva):
        self.level=self.choices.get()
        self.new_game()
        
    def cell_clicked(self,event):
        '''
        make the border of cell in red to see where the cursor is
        '''
        if self.__game.game_over:
            return
        
        x,y=event.x,event.y
        
        if MARGIN<x<WIDTH-MARGIN and MARGIN<y<HEIGHT-MARGIN:
            self.canvas.focus_set()
            row,col=int((y-MARGIN)/SIDE),int((x-MARGIN)/SIDE)
            
            if (row,col)==(self.row,self.col):
                self.row,self.col=-1,-1
            
            if self.__game.puzzle[row][col]==0:
                self.row,self.col=row,col
        else:
            self.row,self.col=-1,-1
           
        self.draw_cursor()
        
    def draw_cursor(self):
        self.canvas.delete("cursor")
        if self.row>=0 and self.col>=0:
            x0=MARGIN+self.col*SIDE+1
            y0=MARGIN+self.row*SIDE+1
            x1=MARGIN+(self.col+1)*SIDE-1
            y1=MARGIN+(self.row+1)*SIDE-1
            self.canvas.create_rectangle(x0,y0,x1,y1,outline="red",tags="cursor")
            
    def key_pressed(self,event):
        if self.__game.game_over:
            return
        
        if self.row>=0 and self.col>=0 and event.char in "1234567890":
            self.__game.start_puzzle[self.row][self.col]=int(event.char)
            self.row,self.col=-1,-1
            self.draw_puzzle()
            self.draw_cursor()
            if self.__game.check_win():
                self.draw_victory()
            elif self.__game.check_win()==False:
                self.draw_defeat()
            
    def draw_defeat(self):
        x0=y0=MARGIN+SIDE*2
        x1=y1=MARGIN+SIDE*7
        self.canvas.create_oval(x0,y0,x1,y1,fill="dark green",outline="black")
        
        x=y=MARGIN+4*SIDE+SIDE/2
        self.canvas.create_text(x,y,text="You lost!",fill="white",font=("Verdana",30))

        
    def draw_victory(self):
        x0=y0=MARGIN+SIDE*2
        x1=y1=MARGIN+SIDE*7
        self.canvas.create_oval(x0,y0,x1,y1,fill="dark green",outline="black")
        
        x=y=MARGIN+4*SIDE+SIDE/2
        self.canvas.create_text(x,y,text="You win!",fill="white",font=("Verdana",30))

        
                
        
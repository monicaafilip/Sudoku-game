'''
Created on Feb 23, 2018

@author: Monica
'''
from sudokuGame.sudokuGame import sudokuGame
from tkinter import Tk
from basics.userInterface import sudokuUi

if __name__ == '__main__':
   
    #the initial level will be beginner
    #the user can change it after starting playing
    game=sudokuGame("beginner")
    game.start()
    
    root=Tk()
    sudokuUi(root,game,"beginner").new_game()
    
    root.mainloop()
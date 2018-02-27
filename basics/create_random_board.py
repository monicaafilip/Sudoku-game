'''
Created on Feb 25, 2018

@author: Monica
'''
import random
from sudokuSolver.solveSudoku import solve
import copy
class create_board:
    '''
    create a random board with the given level
    '''
    def __init__(self,level):
        self.__level = level
        
    def create(self):
        number=0      #keeps how many values will have the board 
        level=self.__level
        if level=="beginner":
            number=40
        elif level=="intermediate":
            number=52
        elif level=="advanced":
            number=65
            
        board,solved_board=self.create_board(number)

        return board,solved_board
        
        
    def create_board(self,number):
        board=[]
        count=9
        while count!=0:
            board.append([0]*9)
            count-=1
        verif=False
        while not verif:
            count=4  #we put first 4 random values in the first 4 positions from the first line after solving it
            row=0
            col=0
            while count!=0:
                value=random.randint(1,9)
                
                board[row][col]=value
                count-=1
                col+=1
                
            verif,solved_board=self.verify_board(board)
            if verif:
                board=self.delete_some_values(solved_board,number)
                
        return board,solved_board
    
    def verify_board(self,board):
        sol=solve(board)
        if sol.backtracking():
            return True,board
        else:
            return False,board
        
    
    def delete_some_values(self,solved,number):
        '''
        delete from the solved board a number of value to be in the given level
        
        '''
        board=copy.deepcopy(solved)
        while number!=0:
            row=random.randint(0,8)
            col=random.randint(0,8)
            if board[row][col]!=0:
                board[row][col]=0
                number-=1
                
        return board

        
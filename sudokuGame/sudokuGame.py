'''
Created on Feb 23, 2018

@author: Monica
'''
from basics.create_random_board import create_board
import copy
class sudokuGame:
    def __init__(self,level):
        self.start_puzzle,self.solved_puzzle=create_board(level).create()
        self.puzzle=copy.deepcopy(self.start_puzzle)

        
    def start(self):
        self.game_over=False
        
        for i in range(9):
            self.puzzle.append([])
            
            for j in range(9):
                self.puzzle[i].append(self.start_puzzle[i][j])
                
    def check_win(self):
        for i in range(9):
            for j in range(9):
                if self.start_puzzle[i][j]==0:
                    return None
        if self.start_puzzle==self.solved_puzzle:
            return True
        return False
            
            
    
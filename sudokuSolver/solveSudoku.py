'''
Created on Feb 24, 2018

@author: Monica
'''
class solve:
    '''
    solve the board given
    return True if the board can be solved,
    else False
    '''
    def __init__(self,sudoku_board):
        self.__sudoku_board = sudoku_board
        
    def final_solution(self):
        for i in range(9):
            for j in range(9):
                if self.__sudoku_board[i][j]==0:
                    return False
        return True
    
    def valid_solution(self,row,column):
        
        appearancesRow,appearancesCol,appearancesSquare=[0]*10,[0]*10,[0]*10
        for i in range(9):
            appearancesRow[self.__sudoku_board[row][i]]+=1
            appearancesCol[self.__sudoku_board[i][column]]+=1
            
            
        for k in range(row-row%3,row-row%3+3):
            for l in range(column-column%3,column-column%3+3):
                appearancesSquare[self.__sudoku_board[k][l]]+=1
                
        for i in range(1,10):
            if appearancesRow[i]>1 or appearancesCol[i]>1 or appearancesSquare[i]>1:
                return False
            
        return True
    
    def getFirstEmpty(self):
        for line in range(9):
            for coll in range(9):
                if self.__sudoku_board[line][coll]==0:
                    return True,line,coll
        return False,-1,-1
    
    
    def backtracking(self):
        get,row,col=self.getFirstEmpty()
        if not get:
            return True
        
        for digit in range(1,10):
            self.__sudoku_board[row][col]=digit
            if self.valid_solution(row, col):
                if self.final_solution():
                    return True
                else:
                    if self.backtracking():
                        return True
            self.__sudoku_board[row][col]=0
            
        return False


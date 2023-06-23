# Name: Joshua Hsueh
# Date: 1/5/2021

import random
import math
class RandomPlayer:
   def __init__(self):
      self.O = "O"
      self.X = "X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite = {self.O: self.X, self.X: self.O}

   def best_strategy(self, board, color):
      # returns best move
      moves = self.find_moves(board, color)
      random.seed()
      move = random.choice(list(moves))
      x = int(move/len(board))
      y = move % len(board)
      ''' Your code goes here ''' 
      best_move = [x, y] # change this
      return best_move, 0

   def find_moves(self, board, color):
      moves_found = {}
      for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==".":
               if j==len(board[0])-1:
                  if board[i][j-1]==".":
                     moves_found[i*len(board)+j]=1
               else:
                  right = True
                  if j==0:
                     right = True
                  elif board[i][j-1]!=".":
                     right = False
                  for y in range(j+1,len(board[0])):
                     if board[i][y]==".":
                        right = False
                  if(right):
                     moves_found[i*len(board)+j]=1
      return moves_found       
    
class CustomPlayer:

   def __init__(self):
      self.O = "O"
      self.X = "X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite = {self.O: self.X, self.X: self.O}

   def best_strategy(self, board, color):
    # returns best move
      move = self.alphabeta(board, color, 5, -1*math.inf, math.inf)
      x = int(move/len(board))
      y = move % len(board)
      ''' Your code goes here ''' 
      best_move = [x, y] # change this
      return best_move, 0
   def terminal_test(self, state):
      directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      for i in range(0,len(state)):
         for j in range(0,len(state[i])):
            if state[i][j]!=".":
               turn = state[i][j]
               for x in directions:
                  count = 0
                  a=i
                  b=j
                  stop = False
                  while(a>=0 and a<len(state) and b>=0 and b<len(state[0])):
                     if(state[a][b]!=turn):
                        stop = True
                     if(not stop):
                        count = count+1
                     a = a + x[0]
                     b = b + x[1]
                  if(count>=4):
                     return True
      for i in range(0,len(state)):
         for j in range(0,len(state[i])):
            if state[i][j]==".":
               return False
      return True
   def alphabeta(self, board, color, search_depth, alpha, beta):
    # returns best "value" while also pruning
     best_move = self.max(board, color, search_depth, alpha, beta)
     return best_move[1]

   def max(self, board, color, search_depth, alpha, beta):
      if self.terminal_test(board) or search_depth==0:
         return self.score(board, color) , None
      possible_moves = self.find_moves(board, color)
      v = -1*math.inf
      move = None
      for a in possible_moves:
         next = self.min(self.make_move(board, color, a), self.opposite[color], search_depth-1, alpha, beta)
         v = max(v, next[0])
         if v==next[0]:
            move = a
         if v>beta: return v, move
         alpha = max(alpha, v)
      return v, move
         
         
   def min(self, board, color, search_depth, alpha, beta):
      if self.terminal_test(board) or search_depth==0:
         return -1*self.score(board, color) , None
      possible_moves = self.find_moves(board, color)
      v = math.inf
      move = None
      for a in possible_moves:
         next = self.max(self.make_move(board, color, a), self.opposite[color], search_depth-1, alpha, beta)
         v = min(v, next[0])
         if v==next[0]:
            move = a
         if v<alpha: return v, move
         beta = min(beta, v)
      return v, move
      

   def make_move(self, board, color, move):
      newboard =[[board[j][i] for i in range(0,len(board[j]))] for  j in range(len(board))]
      newboard[int(move/len(board))][move%len(board)]=color
      return newboard

   def evaluate(self, board, color, possible_moves):
      # returns the utility value  
      return 1

   def score(self, state, color):
    # returns the score of the board 
      directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      score = 0
      for i in range(0,len(state)):
         for j in range(0,len(state[i])):
            if state[i][j]!=".":
               turn = state[i][j]
               for x in directions:
                  count = 0
                  a=i
                  b=j
                  stop = False
                  while(a>=0 and a<len(state) and b>=0 and b<len(state[0])):
                     if(state[a][b]!=turn):
                        stop = True
                     if(not stop):
                        count = count+1
                     a = a + x[0]
                     b = b + x[1]
                  new = 0
                  if(state[i][j]==color):
                     if(count==2):
                        new = 2/2
                     elif(count==3):
                        new = 5/3
                     elif(count==4):
                        new = 100
                  else:
                     if(count==3):
                        new = -4/3  
                     elif(count==4):
                        new = -100                  
                  score = score + new
      return score            

   def find_moves(self, board, color):
      moves_found = {}
      for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==".":
               if j==len(board[0])-1:
                  if board[i][j-1]==".":
                     moves_found[i*len(board)+j]=1
               else:
                  right = True
                  if j==0:
                     right = True
                  elif board[i][j-1]!=".":
                     right = False
                  for y in range(j+1,len(board[0])):
                     if board[i][y]==".":
                        right = False
                  if(right):
                     moves_found[i*len(board)+j]=1
      return moves_found  
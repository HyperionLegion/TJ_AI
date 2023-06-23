# Name: Joshua Hsueh
# Date: 1/5/2021

import random
import math
class RandomBot:
   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None

   def best_strategy(self, board, color):
      # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])
      if color == "#000000":
         color = "@"
      else:
         color = "O"
      moves = self.find_moves(board, color)
      random.seed()
      move = random.choice(list(moves))
      x = int(move/len(board))
      y = move % len(board)
      ''' Your code goes here ''' 
      best_move = [x, y] # change this
      return best_move, 0

   def stones_left(self, board):
    # returns number of stones that can still be placed (empty spots)
      count = 0
      for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j]==".":
               count = count+1
      return count

   def find_moves(self, board, color):
      moves_found = {}
      for i in range(len(board)):
        for j in range(len(board[i])):
            flipped_stones = self.find_flipped(board, i, j, color)
            if len(flipped_stones) > 0:
                moves_found.update({i*self.y_max+j: flipped_stones})
      return moves_found       
               
   def find_flipped(self, board, x, y, color):
      if board[x][y] != ".":
         return []
      flipped_stones = []
      for incr in self.directions:
        temp_flip = []
        x_pos = x + incr[0]
        y_pos = y + incr[1]
        while 0 <= x_pos < self.x_max and 0 <= y_pos <self. y_max:
            if board[x_pos][y_pos] == ".":
                break
            if board[x_pos][y_pos] == color:
                flipped_stones += temp_flip
                break
            temp_flip.append([x_pos, y_pos])
            x_pos += incr[0]
            y_pos += incr[1]
      return flipped_stones
    
class Best_AI_bot:

   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None

   def best_strategy(self, board, color):
    # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])
      if color == "#000000":
         color = "@"
      else:
         color = "O"
      move = self.alphabeta(board, color, 4, -1*math.inf, math.inf)
      x = int(move/len(board))
      y = move % len(board)
      ''' Your code goes here ''' 
      best_move = [x, y] # change this
      return best_move, 0

   def minimax(self, board, color, search_depth):
    # returns best "value"
      return 1

   def negamax(self, board, color, search_depth):
    # returns best "value"
      return 1
      
   def alphabeta(self, board, color, search_depth, alpha, beta):
    # returns best "value" while also pruning
     best_move = self.max(board, color, search_depth, alpha, beta)
     print(best_move)
     return best_move[1]

   def max(self, board, color, search_depth, alpha, beta):
      if self.stones_left(board)==0 or search_depth==0:
         return self.score(board, color) , None
      possible_moves = self.find_moves(board, color)
      v = -1*math.inf
      move = None
      for a in possible_moves:
         next = self.min(self.make_move(board, color, a, self.find_flipped(board, int(a/len(board)), a%len(board), color)), self.opposite_color[color], search_depth-1, alpha, beta)
         v = max(v, next[0])
         if v==next[0]:
            move = a
         if v>beta: return v, move
         alpha = max(alpha, v)
      return v, move
         
         
   def min(self, board, color, search_depth, alpha, beta):
      if self.stones_left(board)==0 or search_depth==0:
         return -1*self.score(board, color) , None
      possible_moves = self.find_moves(board, color)
      v = math.inf
      move = None
      for a in possible_moves:
         next = self.max(self.make_move(board, color, a, self.find_flipped(board, int(a/len(board)), a%len(board), color)), self.opposite_color[color], search_depth-1, alpha, beta)
         v = min(v, next[0])
         if v==next[0]:
            move = a
         if v<alpha: return v, move
         beta = min(beta, v)
      return v, move
      
   def make_key(self, board, color):
    # hashes the board
      return 1

   def stones_left(self, board):
    # returns number of stones that can still be placed
      count = 0
      for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j]==".":
               count = count+1
      return count

   def make_move(self, board, color, move, flipped):
      newboard =[[board[i][j] for i in range(0,len(board[j]))] for  j in range(len(board))]
      newboard[int(move/len(board))][move%len(board)]=color
      for i in flipped:
         newboard[int(move/len(board))][move%len(board)] = color
      return newboard

   def evaluate(self, board, color, possible_moves):
      # returns the utility value  
      return 1

   def score(self, board, color):
    # returns the score of the board 
      count = 0
      for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j]!=".":
               if board[i][j]==color:
                  count=count+1
               else:
                  count=count-1      
      return count

   def find_moves(self, board, color):
      moves_found = {}
      for i in range(len(board)):
        for j in range(len(board[i])):
            flipped_stones = self.find_flipped(board, i, j, color)
            if len(flipped_stones) > 0:
                moves_found.update({i*self.y_max+j: flipped_stones})
      return moves_found       
               
   def find_flipped(self, board, x, y, color):
      if board[x][y] != ".":
         return []
      flipped_stones = []
      for incr in self.directions:
        temp_flip = []
        x_pos = x + incr[0]
        y_pos = y + incr[1]
        while 0 <= x_pos < self.x_max and 0 <= y_pos <self. y_max:
            if board[x_pos][y_pos] == ".":
                break
            if board[x_pos][y_pos] == color:
                flipped_stones += temp_flip
                break
            temp_flip.append([x_pos, y_pos])
            x_pos += incr[0]
            y_pos += incr[1]
      return flipped_stones


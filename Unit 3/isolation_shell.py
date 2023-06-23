# Name: Joshua Hsueh
# Date: 12/15/2020
import random
import math
class RandomPlayer:
   def __init__(self):
      self.white = "O"
      self.black = "X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None
      self.first_turn = True
      
   def best_strategy(self, board, color):
      random.seed()
      moves =self.find_moves(board, color)
      best_move = random.choice(list(moves))
      y = int(best_move/len(board))
      x = best_move % len(board)
      
      #(column num 0-4, row num 0-4)
      return (x,y), 0
      
      
   def find_moves(self, board, color):
       moves_found = set()
       turn = "O"
       if color == "#000000":
         turn = "X"
       for i in range(len(board)):
           for j in range(len(board[i])):
               found = False
               for x in board:
                  if turn in x:
                     found = True
               if (not found) and board[i][j]==".":
                  moves_found.add(j*len(board)+i)
               elif (turn == self.black and board[i][j] == 'X') or (turn == self.white and board[i][j] == 'O'):
                   for incr in self.directions:
                       x_pos = i + incr[0]
                       y_pos = j + incr[1]
                       stop = False
                       while 0 <= x_pos < len(board) and 0 <= y_pos < len(board):
                           if board[x_pos][y_pos] != '.':
                              stop = True
                           if not stop:
                              moves_found.add(y_pos*(len(board))+x_pos)
                           x_pos += incr[0]
                           y_pos += incr[1]
                           
         #{0, 1, 2, ... 24}
       return moves_found
       
class CustomPlayer:

   def __init__(self):
      self.white = "O"
      self.black = "X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None
      self.first_turn = True

   def best_strategy(self, board, color):
      # returns best move
      turn = "O"
      if color =="#000000":
         turn = "X" 
      #best_move = self.max_value(board, turn, 3)
      best_move = self.negamax(board, turn, 3)
      #best_move = self.alphabeta(board, turn, 3, -math.inf, math.inf)
      return best_move

   def minimax(self, board, color, search_depth):
      # returns best "value"
      best_move = self.max_value(board, color, search_depth)
      return best_move
   def max_value(self, board, color, search_depth):      
      possible_moves = self.find_moves(board, color)
      opponent = self.opposite_color[color]
      if search_depth==0 or len(possible_moves)==0:
         return (len(board)), (len(board[0])), self.evaluate(board, color, possible_moves)
      v= -math.inf
      move = None
      for a in possible_moves:
         y = int(a/len(board))
         x = a % len(board)
         next = self.min_value(self.make_move(board, color, (x, y)), opponent, search_depth-1)
         board[x][y]="."
         v=max(v, next[1])
         if v ==next[1]:
            move = (x, y)
      return move, v
     
   def min_value(self, board, color, search_depth):      
      possible_moves = self.find_moves(board, color)
      opponent = self.opposite_color[color]
      if search_depth==0 or len(possible_moves)==0:
         return (len(board)), (len(board[0])), -1*self.evaluate(board, color, possible_moves)
      v= math.inf
      move = None
      for a in possible_moves:
         y = int(a/len(board))
         x = a % len(board)
         next = self.max_value(self.make_move(board, color, (x, y)), opponent, search_depth-1)
         board[x][y]="."
         v=min(v, next[1])
         if v ==next[1]:
            move = (x, y)
      return move, v

   def negamax(self, board, color, search_depth):
      # returns best "value"
      possible_moves = self.find_moves(board, color)
      opponent = self.opposite_color[color]
      if search_depth==0 or len(possible_moves)==0:
         return (len(board), len(board[0])), self.evaluate(board, color, possible_moves)
      v = -math.inf
      move = None
      for a in possible_moves:
         y = int(a/len(board))
         x = a % len(board)
         next = self.negamax(self.make_move(board, color, (x, y)), opponent, search_depth-1)
         board[x][y]="."
         v = max(v, -1*next[1])
         if v == -1*next[1]:
            move = (x, y)
      return move, v
      
   # def alphabeta(self, board, color, search_depth, alpha, beta):
#       possible_moves = self.find_moves(board, color)
#       opponent = self.opposite_color[color]
#       if search_depth==0 or len(possible_moves)==0:
#          return (len(board), len(board[0])), self.evaluate(board, color, possible_moves)
#       move = None
#       v = -1*math.inf
#       for a in possible_moves:
#          y = int(a/len(board))
#          x = a % len(board)
#          next = self.alphabeta(self.make_move(board, color, (x, y)), opponent, search_depth-1, -1*beta, -1*alpha)
#          v = max(v, -1*next[1])
#          board[x][y]="."
#          alpha = max(alpha, v)
#          if v == -1*next[1]:
#             move = (x, y)
#          if alpha >= beta:
#             break
#       return move, alpha

   
   def alphabeta(self, board, color, search_depth, alpha, beta):
      # returns best "value"
      best_move = self.alpha(board, color, search_depth, alpha, beta)
      return best_move
   def alpha(self, board, color, search_depth, alpha, beta):      
       possible_moves = self.find_moves(board, color)
       opponent = self.opposite_color[color]
       if search_depth==0 or len(possible_moves)==0:
          return (len(board)), (len(board[0])), self.evaluate(board, color, possible_moves)
       move = None
       value = -math.inf
       for a in possible_moves:
          y = int(a/len(board))
          x = a % len(board)
          next = self.beta(self.make_move(board, color, (x, y)), opponent, search_depth-1, alpha, beta)
          board[x][y]="."
          value = max(value, next[1])
          alpha=max(alpha, value)
          if value ==next[1]:
             move = (x, y)
          if alpha >= beta:
             break
       return move, value
      
   def beta(self, board, color, search_depth, alpha, beta):      
       possible_moves = self.find_moves(board, color)
       opponent = self.opposite_color[color]
       if len(possible_moves)==0 or search_depth==0:
          return (len(board)), (len(board[0])), -1*self.evaluate(board, color, possible_moves)
       move = None
       value = math.inf
       for a in possible_moves:
          y = int(a/len(board))
          x = a % len(board)
          next = self.alpha(self.make_move(board, color, (x, y)), opponent, search_depth-1, alpha, beta)
          board[x][y]="."
          value = min(value, next[1])
          beta=min(beta, value)
          if value ==next[1]:
             move = (x, y)
          if beta <= alpha:
             break
       return move, value

   def make_move(self, board, color, move):
      #return board
      # returns board that has been updated
      board[move[0]][move[1]] = color
      return board

   def evaluate(self, board, color, possible_moves):
      # returns the utility value
      opponent = self.opposite_color[color]
      return len(possible_moves) - len(self.find_moves(board, opponent))

   def find_moves(self, board, color):
       moves_found = set()
       turn = color
       for i in range(len(board)):
           for j in range(len(board[i])):
               found = False
               for x in board:
                  if turn in x:
                     found = True
               if (not found) and board[i][j]==".":
                  moves_found.add(j*len(board)+i)
               elif (turn == self.black and board[i][j] == 'X') or (turn == self.white and board[i][j] == 'O'):
                   for incr in self.directions:
                       x_pos = i + incr[0]
                       y_pos = j + incr[1]
                       stop = False
                       while 0 <= x_pos < len(board) and 0 <= y_pos < len(board):
                           if board[x_pos][y_pos] != '.':
                              stop = True
                           if not stop:
                              moves_found.add(y_pos*(len(board))+x_pos)
                           x_pos += incr[0]
                           y_pos += incr[1]
                           
         #{0, 1, 2, ... 24}
       return moves_found


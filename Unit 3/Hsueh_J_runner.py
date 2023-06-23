import sys
import os
from Hsueh_J_player import CustomPlayer, RandomPlayer
def display(state):
   str = ""
   for j in range(0,6):
      for i in range(0,7):
         str = str + " " + state[i][j]
      str = str+"\n"
   return str
def terminal_test(state):
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
def utility(state):
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
                  return 1
   return 0
def domove(move, state, turn):
   state[move[0]][move[1]]=turn
   return state
def main():
   X = input("X is random or AI? (r: random, a: AI) ")
   O = input("O is random or AI? (r: random, a: AI) ")
   state = [["." for j in range(0,6)] for i in range(0,7)]
   turn = "X"
   players = {}
   if X == 'a':
      players[0] = CustomPlayer()
   else:
      players[0] = RandomPlayer()
   if O=='a':
      players[1] = CustomPlayer()
   else:
      players[1] = RandomPlayer() 
   print ("Game start!")
   print (display(state))
   while terminal_test(state) == False:
       if turn == 'X':
          print ("{}'s turn:".format(turn))
          move, idc = players[0].best_strategy(state, turn)
          state = domove(move, state, turn)
          print (display(state))
          turn = 'O'
       else:
          print ("{}'s turn:".format(turn))
          move, idc = players[1].best_strategy(state, turn)
          state = domove(move, state, turn)
          print (display(state))
          turn = 'X'
          
   if utility(state) == 0:
       print ("Game over! Tie!")
   else: 
       turn = 'O' if turn == 'X' else 'X'
       print ('Game over! ' + turn + ' win!')
if __name__ =='__main__':
   main()
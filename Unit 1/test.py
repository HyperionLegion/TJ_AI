import random

def getInitialState():
   x = "_12345678"
   l = list(x)
   random.shuffle(l)
   y = ''.join(l)
   return y
   
'''precondition: i<j
   swap characters at position i and j and return the new state'''
def swap(state, i, j):
   '''your code goes here'''
   return state[:i]+state[j]+state[i+1:j]+state[i]+state[j+1:];
   
'''Generate a list which hold all children of the current state
   and return the list'''
def generate_children(state):
   '''your code goes here'''
   children = []
   if(state.index("_")-3>=0): children.append(swap(state, state.index("_")-3, state.index("_")))
   if(state.index("_")%3!=0): children.append(swap(state, state.index("_")-1, state.index("_")))
   if(state.index("_")+3<=8): children.append(swap(state, state.index("_"), state.index("_")+3))
   if((state.index("_")+1)%3!=0): children.append(swap(state, state.index("_"), state.index("_")+1))


   return children
   
def display_path(n, explored): #key: current, value: parent
   l = []
   while explored[n] != "s": #"s" is initial's parent
      l.append(n)
      n = explored[n]
   print ()
   l = l[::-1]
   for i in l:
      print (i[0:3], end = "   ")
   print ()
   for j in l:
      print (j[3:6], end = "   ")
   print()
   for k in l:
      print (k[6:9], end = "   ")
   print ("\n\nThe shortest path length is :", len(l))
   return ""

'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling display_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''
def BFS(initial_state):
   explored = {}
   q = [initial_state];
   explored[initial_state]="s"
   while True:
      if len(q)==0: return ("Fail")
      s = q.pop(0)
      if s=="_12345678":
         return display_path(s, explored) 
      for a in generate_children(s):
         if a not in explored:
            q.append(a) 
            explored[a]=s

'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling display_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''
def DFS(initial):
   explored = {}
   q = [initial]
   explored[initial] = "s"
   while True:
      if len(q)==0: return ("Fail")
      s = q.pop()
      if s=="_12345678":
         return display_path(s, explored) 
      for a in generate_children(s):
         if a not in explored:
          q.append(a) 
          explored[a] = s


def main():
   initial = getInitialState()
   print ("BFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
   print (BFS(initial))
   print ("DFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
   print (DFS(initial))

if __name__ == '__main__':
   main()

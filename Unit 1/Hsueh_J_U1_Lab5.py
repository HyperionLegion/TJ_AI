# Name: Joshua Hsueh         Date: 10/16/2020
import time

def generate_adjacents(current, words_set):
   ''' words_set is a set which has all words.
   By comparing current and words in the words_set,
   generate adjacents set of current and return it'''
   adj_set = set()
   for j in range(len(current)):
      alphabet = "abcdefghijklmnopqrstuvwxyz"
      for i in range(len(alphabet)):
         if((current[:j]+alphabet[i]+current[j+1:]) in words_set and alphabet[i]!=current[j]):
            adj_set.add(current[:j]+alphabet[i]+current[j+1:])
   # TODO 1: adjacents
   # Your code goes here
   return adj_set

def check_adj(words_set):
   # This check method is written for words_6_longer.txt
   adj = generate_adjacents('listen', words_set)
   print(adj)
   target =  {'listee', 'listel', 'litten', 'lister', 'listed'}
   return (adj == target)

def bi_bfs(start, goal, words_set):
   '''The idea of bi-directional search is to run two simultaneous searches--
   one forward from the initial state and the other backward from the goal--
   hoping that the two searches meet in the middle. 
   '''
   if start == goal: return []
   forward, backward = [start], [goal]
   explored1, explored2 = {start:0}, {goal:1}
   while len(forward)!=0 and len(backward)!=0:
      temp = forward[:]
      forward=[]
      while len(temp)>0:
         s = temp.pop(0)
         if s in backward:
            path = []
            g = s
            while(s!=0):
               path = [s] + path
               s = explored1[s]
            g = explored2[g]
            while(g!=1):
               path = path + [g]
               g = explored2[g]
            return path
         children = generate_adjacents(s, words_set)
         for a in children:
            if a not in explored1:
               forward.append(a)
               explored1[a] = s
      temp = backward[:]
      backward = []
      while len(temp)>0:
         s = temp.pop(0)
         if s in forward:
            path = []
            g = s
            while(g!=1):
               path = path + [g]
               g = explored2[g]
            s = explored1[s]
            while(s!=0):
               path = [s] + path
               s = explored1[s]
            return path
         children = generate_adjacents(s, words_set)
         for a in children:
            if a not in explored2:
               backward.append(a)
               explored2[a] = s

   # TODO 2: Bi-directional BFS Search
   # Your code goes here
   return None

def main():
   filename = input("Type the word file: ")
   words_set = set()
   file = open(filename, "r")
   for word in file.readlines():
      words_set.add(word.rstrip('\n'))
   #print ("Check generate_adjacents():", check_adj(words_set))
   initial = input("Type the starting word: ")
   goal = input("Type the goal word: ")
   cur_time = time.time()
   path = (bi_bfs(initial, goal, words_set))
   if path != None:
      print (path)
      print ("The number of steps: ", len(path))
      print ("Duration: ", time.time() - cur_time)
   else:
      print ("There's no path")
 
if __name__ == '__main__':
   main()

'''
Sample output 1
Type the word file: words.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'listed', 'fisted', 'fitted', 'fitter', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  9
Duration: 0.0

Sample output 2
Type the word file: words_6_longer.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'lister', 'bister', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  7
Duration: 0.000997304916381836

Sample output 3
Type the word file: words_6_longer.txt
Type the starting word: vaguer
Type the goal word: drifts
['vaguer', 'vagues', 'values', 'valves', 'calves', 'cauves', 'cruves', 'cruses', 'crusts', 'crufts', 'crafts', 'drafts', 'drifts']
The number of steps:  13
Duration: 0.0408782958984375

Sample output 4
Type the word file: words_6_longer.txt
Type the starting word: klatch
Type the goal word: giggle
['klatch', 'clatch', 'clutch', 'clunch', 'glunch', 'gaunch', 'paunch', 'paunce', 'pawnce', 'pawnee', 'pawned', 'panned', 'panged', 'ranged', 'ragged', 'raggee', 'raggle', 'gaggle', 'giggle']
The number of steps:  19
Duration:  0.0867915153503418
'''
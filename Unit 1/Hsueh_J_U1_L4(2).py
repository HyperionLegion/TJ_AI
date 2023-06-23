# Name: Joshua Hsueh         Date: 10/10/2020
import random, time, math
class HeapPriorityQueue():
   
   def __init__(self):
      self.queue = ["dummy"]  # we do not use index 0 for easy index calulation
      self.current = 1        # to make this object iterable

   def next(self):            # define what __next__ does
      if self.current >=len(self.queue):
         self.current = 1     # to restart iteration later
         raise StopIteration
    
      out = self.queue[self.current]
      self.current += 1
   
      return out

   def __iter__(self):
      return self

   __next__ = next

   def isEmpty(self):
      return len(self.queue) == 1    # b/c index 0 is dummy

   def swap(self, a, b):
      self.queue[a], self.queue[b] = self.queue[b], self.queue[a]

   # Add a value to the heap_pq
   def push(self, value):
      self.queue.append(value)
      self.heapUp(len(self.queue)-1)
      # write more code here to keep the min-heap property

   # helper method for push      
   def heapUp(self, k):
      parent = k//2
      if parent !=0:  
         if(self.queue[parent][1]>self.queue[k][1]):
            self.swap(parent, k)
            self.heapUp(parent) 
               
   # helper method for reheap and pop
   def heapDown(self, k, size):
      left, right = 2*k, 2*k+1
      if left==size and self.queue[k][1]>self.queue[size][1]:
         self.swap(k,size)
      elif right <=size:
         minC = (left if self.queue[left][1]<=self.queue[right][1] else right)
         if self.queue[k][1] > self.queue[minC][1]:
            self.swap(k, minC)
            self.heapDown(minC, size)

   
   # make the queue as a min-heap            
   def reheap(self):
      for k in range((len(self.queue)-1)//2,0,-1):
         heapDown(array, k, len(self.queue)-1)
   
   # remove the min value (root of the heap)
   # return the removed value            
   def pop(self):
      # Your code goes here
      self.swap(1, len(self.queue)-1)
      x = self.queue.pop()
      self.heapDown(1, len(self.queue)-1)
      return x   # change this
   
# This method is for testing. Do not change it.
def isHeap(heap, k):
   left, right = 2*k, 2*k+1
   if left == len(heap): return True
   elif len(heap) == right and heap[k] > heap[left]: return False
   elif right < len(heap): 
      if (heap[k][1] > heap[left][1] or heap[k][1] > heap[right][1]): return False
      else: return isHeap(heap, left) and isHeap(heap, right)
   return True

def getInitialState(sample, size):
   sample_list = list(sample)
   random.shuffle(sample_list)
   new_state = ''.join(sample_list)
   while not inversion_count(new_state, size, size): 
      random.shuffle(sample_list)
      new_state = ''.join(sample_list)
   return new_state
   
'''precondition: i<j
   swap characters at position i and j and return the new node'''
def swap(node, i, j):
   '''your code goes here'''
   return node[:i]+node[j]+node[i+1:j]+node[i]+node[j+1:];
   
'''Generate a list which hold all children of the current node
   and return the list'''
def generate_children(node, size=4):
   '''your code goes here'''
   children = []
   if(node.index("_")-size>=0): children.append(swap(node, node.index("_")-size, node.index("_")))
   if(node.index("_")%size!=0): children.append(swap(node, node.index("_")-1, node.index("_")))
   if(node.index("_")+size<=len(node) - 1): children.append(swap(node, node.index("_"), node.index("_")+size))
   if((node.index("_")+1)%size!=0): children.append(swap(node, node.index("_"), node.index("_")+1))


   return children
   
def display_path(path_list, size=4):
   for i in range(size):
      for j in path_list:
         print (j[i*size:(i+1)*size], end = "   ")
      print()
   print ("\n\nThe shortest path length is :", len(path_list))
   return ""
def dist_heuristic(start, goal="_123456789ABCDEF", size=4):
   count=0
   for i in range(0,len(start)):
      j = goal.index(start[i])
      y = 0
      while(int(i/size)!=int(j/size)):
         y=y+1
         if(j>i):
            j=j-size
         else:
            j=j+size
      x = abs(i-j)
      count = count+((x**2+y**2)**1/2)
   return count
def check_heuristic():
   a = dist_heuristic("152349678_ABCDEF", "_123456789ABCDEF", 4)
   b = dist_heuristic("8936C_24A71FDB5E", "_123456789ABCDEF", 4)
   return (a < b)
def check_inversion():
   t1 = inversion_count("_42135678", 3, 3)  # N=3
   f1 = inversion_count("21345678_", 3, 3)
   t2 = inversion_count("4123C98BDA765_EF", 4) # N is default, N=4
   f2 = inversion_count("4123C98BDA765_FE", 4)
   return t1 and t2 and not (f1 or f2)
def a_star(start, goal="_123456789ABCDEF", heuristic=dist_heuristic, size=4):
   frontier = HeapPriorityQueue()
   if start == goal: return []
   explored = {}
   explored[start]=("s", 0)
   frontier.push([start, 0])
   while len(frontier.queue)!=0:
      s = frontier.pop()
      if s[0]==goal:
         path = []
         x = s[0]
         while(x!="s"):
            path=[x]+path
            x = explored[x][0]
         return path 
      for a in generate_children(s[0], size):
         if a not in explored or (a in explored and explored[a][1]>explored[s[0]][1]+1):
            explored[a]=(s[0], explored[s[0]][1]+1)
            frontier.push((a, explored[a][1]+(heuristic(a, goal, size)))) 
   return None
   #check path (closed set) before add a new node to frontier
def inversion_count(node, width=4, N=4):
   count = 0
   for i in range(N*width):
      if node[i]!="_":
         for j in range(i+1,N*width):
            if node[j]!="_":
               count = count + 1 if node[j]<node[i] else count 
   if N%2==0:
      if((N-int(node.index("_")/width))%2==0):
         return count%2==0
      else:
         return count%2!=0
   else:
      return count%2==0
      
def main():
   # A star
   print ("Inversion works?:", check_inversion())
   print ("Heuristic works?:", check_heuristic())
   #initial_state = getInitialState("_123456789ABCDEF", 4)
   initial_state = input("Type initial state: ")
   if inversion_count(initial_state):
      cur_time = time.time()
      path = (a_star(initial_state))
      if path != None: display_path(path, 4)
      else: print ("No Path Found.")
      print ("Duration: ", (time.time() - cur_time))
   else: print ("{} did not pass inversion test.".format(initial_state))
   
if __name__ == '__main__':
   main()

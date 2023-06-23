# Name: Joshua Hsueh
# Date: 10/1/2020

import random

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
         if(self.queue[parent]>self.queue[k]):
            self.swap(parent, k)
            self.heapUp(parent) 
               
   # helper method for reheap and pop
   def heapDown(self, k, size):
      left, right = 2*k, 2*k+1
      if left==size and self.queue[k]>self.queue[size]:
         self.swap(k,size)
      elif right <=size:
         minC = (left if self.queue[left]<=self.queue[right] else right)
         if self.queue[k] > self.queue[minC]:
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
      
   # remove a value at the given index (assume index 0 is the root)
   # return the removed value   
   def remove(self, index):
      self.swap(index+1, len(self.queue)-1)
      x = self.queue.pop()
      self.heapDown(index+1, len(self.queue)-1)
      return x     # change this
   
  

# This method is for testing. Do not change it.
def isHeap(heap, k):
   left, right = 2*k, 2*k+1
   if left == len(heap): return True
   elif len(heap) == right and heap[k] > heap[left]: return False
   elif right < len(heap): 
      if (heap[k] > heap[left] or heap[k] > heap[right]): return False
      else: return isHeap(heap, left) and isHeap(heap, right)
   return True
    
# This method is for testing. Do not change it.
def main():
        
   pq = HeapPriorityQueue()    # create a HeapPriorityQueue object
   
   print ("Check if dummy 0 is still dummy:", pq.queue[0])
   
   # assign random integers into the pq
   for i in range(20):
      t = random.randint(10, 99)
      print (t, end=" ")
      pq.push(t)
   
   print ()
   
   # print the pq which is a min-heap
   for x in pq:
      print (x, end=" ")
   print()
   
   # remove test
   print ("Index 4 is removed:", pq.remove(4))
   
   # check if pq is a min-heap
   for x in pq:
      print (x, end=" ")
   print("\nIs a min-heap?", isHeap(pq.queue, 1))
   
   temp = []
   while not pq.isEmpty():
      temp.append(pq.pop())
      print (temp[-1], end=" ")
   
   print ("\nIn ascending order?", temp == sorted(temp))

if __name__ == '__main__':
   main()
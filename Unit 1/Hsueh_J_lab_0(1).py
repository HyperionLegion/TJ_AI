# Name: Joshua Hsueh
# Date: 9/17/2020

# Each Vertex object will have attributes to store its own name and its list of its neighboring vertices.
class Vertex:
   def __init__(self, value=0, neighbors=[]):
      self.value = value
      self.neighbors = neighbors
   

# If the file exists, read all edges and build a graph. It returns a list of Vertexes.   
def build_graph(filename):
   vertexes = []
   with open(filename) as infile:
      lines = infile.readlines() 
      for line in lines:
         x, v1,v2 = [],Vertex(line.strip().split()[0], []),Vertex(line.strip().split()[1], [])
         for vertex in vertexes:
            x.append(vertex.value)
         if v1.value not in x:
            vertexes.append(v1)
            x.append(v1.value)
         if v2.value not in x:
            vertexes.append(v2)
            x.append(v2.value)
         y = []
         for neighbor in vertexes[x.index(v1.value)].neighbors:
            y.append(neighbor)
         if vertexes[x.index(v2.value)] not in y:
            vertexes[x.index(v1.value)].neighbors.append(vertexes[x.index(v2.value)])
   return vertexes

# prints all vertices and adjacent lists of the given graph.
def display_graph(graph):
   for vertex in graph:
      list=[]
      for neighbor in vertex.neighbors:
         list.append(neighbor.value)
      print(vertex.value,list)

# checks if two Vertexes are reachable or not.  
def is_reachable(fromV, toV):
   x, y = set(), []
   y.append(fromV)
   x.add(fromV.value)
   while y:
      z = y.pop()
      if z==toV: return True
      for i in z.neighbors:
         if not i.value in x:
            y.append(i)
            x.add(i.value)
   return False

# returns the length of the path from a Vertex to the other Vertex. 
# If the other Vertex is not reachable, return -1.  (Ex) Path cost of A to B to C is 2. 
def path_cost(fromV, toV):
   if(not is_reachable(fromV, toV)): return -1
   else:
      if(fromV==toV): return 1
      else:
         v = fromV
         path={fromV}
         while v!=toV:
            for vertex in v.neighbors:
               if vertex!=fromV:
                  path.add(vertex if is_reachable(vertex, toV) else None)
                  v=vertex
         return len(path)-1 
# Name: Joshua Hsueh
# Date: 12/1/2020
import os, time
   
def select_unassigned_var( variables):
   return min([(len(n), x) for x, n in variables.items()])[1]

def isValid(value, var_index, assignment, csp_table):
   for x in csp_table[var_index]:
      if str(value) == assignment[x]:
         return False
   return True

def recursive_backtracking(assignment, variables, csp_table, q_table):
   if assignment.find('.')==-1: return assignment
   var = select_unassigned_var( variables)
   list = [(k, v) for k, v in q_table.items() if k in variables[var] and v<10]
   list.sort(key=lambda x:x[1])
   for item in list[::-1]:
      value = item[0]
      if isValid(value, var, assignment, csp_table):
            remove = set()
            for i in csp_table[var]:
               if i in variables and value in variables[i]:
                  variables[i].remove(value)
                  remove.add(i)
            removed = variables[var]
            del variables[var]
            assignment = assignment[:var] + str(value) + assignment[var+1:]
            q_table[value] = q_table[value]+1
            result = recursive_backtracking(assignment, variables, csp_table, q_table)
            if result!=None: return result
            assignment = assignment[:var] + "." + assignment[var+1:]
            q_table[value]=q_table[value]-1
            for i in remove:
               variables[i].add(value)
            variables[var] = removed
   return None

def solve(puzzle, neighbors): 
   ''' suggestion:
   # q_table is quantity table {'1': number of value '1' occurred, ...}
   variables, puzzle, q_table = initialize_ds(puzzle, neighbors)  
   return recursive_backtracking(puzzle, variables, neighbors, q_table)
   '''
   variables = {} # variables
   for x in neighbors:
      if(puzzle[x]=="."):
         variables[x] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
         for y in neighbors[x]:
            if puzzle[y]!="." and int(puzzle[y]) in variables[x]:
               variables[x].remove(int(puzzle[y]))
   q_table = {}
   for i in range(1,10):
      q_table[i] = 0
   return recursive_backtracking(puzzle, variables, neighbors, q_table)

def sudoku_neighbors(csp_table):
   # each position p has its neighbors {p:[positions in same row/col/subblock], ...}
   neighbors = {}
   for i in range(0, 81):
      neighbors[i] = set()
      for x in csp_table:
         if i in x:
            for y in x:
               if y != i:
                  neighbors[i].add(y)
   return neighbors
   
def sudoku_csp(n=9):
   csp_table = [[k for k in range(i*n, (i+1)*n)] for i in range(n)] # rows
   csp_table += [[k for k in range(i,n*n,n)] for i in range(n)] # cols
   temp = [0, 1, 2, 9, 10, 11, 18, 19, 20]
   csp_table += [[i+k for k in temp] for i in [0, 3, 6, 27, 30, 33, 54, 57, 60]] # sub_blocks
   return csp_table

def checksum(solution):
   return sum([ord(c) for c in solution]) - 48*81 # One easy way to check a valid solution

def main():
   filename = input("file name: ")
   if not os.path.isfile(filename):
      filename = "puzzles.txt"
   csp_table = sudoku_csp()   # rows, cols, and sub_blocks
   neighbors = sudoku_neighbors(csp_table)   # each position p has its neighbors {p:[positions in same row/col/subblock], ...}
   start_time = time.time()
   for line, puzzle in enumerate(open(filename).readlines()):
      #if line == 50: break  # check point: goal is less than 0.5 sec
      line, puzzle = line+1, puzzle.rstrip()
      print ("Line {}: {}".format(line, puzzle)) 
      solution = solve(puzzle, neighbors)
      if solution == None:print ("No solution found."); break
      print ("{}({}, {})".format(" "*(len(str(line))+1), checksum(solution), solution))
   print ("Duration:", (time.time() - start_time))

if __name__ == '__main__': main()
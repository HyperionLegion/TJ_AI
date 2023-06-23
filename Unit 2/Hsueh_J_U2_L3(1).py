# Name: Joshua Hsueh
# Date: 11/17/2020

def check_complete(assignment, csp_table):
   if assignment.find('.') != -1: return False
   for hexa in csp_table:
      if len(set([assignment[i] for i in hexa])) != 9: return False
   return True
   
def select_unassigned_var(assignment, variables, csp_table):
   return min([(len(n), x) for x, n in variables.items() if assignment[x]=="."])[1]

def isValid(value, var_index, assignment, variables, csp_table):
   for x in csp_table:
      if var_index in x:
         for y in x:
            if str(value) == assignment[y]:
               return False
   return True


def ordered_domain(assignment, variables, csp_table):
   return []

def update_variables(value, var_index, assignment, variables, csp_table):
   return {}

def backtracking_search(puzzle, variables, csp_table): 
   return recursive_backtracking(puzzle, variables, csp_table)

def recursive_backtracking(assignment, variables, csp_table):
   if check_complete(assignment, csp_table): return assignment
   var = select_unassigned_var(assignment, variables, csp_table)
   for value in variables[var]:
      if isValid(value, var, assignment, variables, csp_table):
         assignment = assignment[:var] + str(value) + assignment[var+1:]
         result = recursive_backtracking(assignment, variables, csp_table)
         if result!=None: return result
         assignment = assignment[:var] + "." + assignment[var+1:]
   return None


def display(solution):
   s = ""
   for x in range(0,9):
      for y in range(0,9):
         s = s + solution[x*9+y] + " "
         if y!=0 and (y+1)%3==0:
            s = s + "   "
      s = s + "\n"
      if x!=0 and (x+1)%3==0:
         s = s+ "\n"
   return s

def sudoku_csp():
   lists= [[0,9,18,27,36,45,54,63,72], [1, 10, 19, 28, 37, 46, 55, 64, 73], [2, 11, 20, 29, 38, 47, 56, 65, 74], [3, 12, 21, 30, 39, 48, 57, 66, 75], [4, 13, 22, 31, 40, 49, 58, 67, 76], [5, 14, 23, 32, 41, 50, 59, 68, 77], [6, 15, 24, 33, 42, 51, 60, 69, 78], [7, 16, 25, 34, 43, 52, 61, 70, 79], [8, 17, 26, 35, 44, 53, 62, 71, 80]] #9 rows, 9 columns, 9 small squares
   for x in range(0,9):
      list = []
      for y in range(0,9):
         list.append(x*9+y)
      lists = lists + [list]
   lists = lists + [[0, 1, 2, 9, 10, 11, 18, 19, 20], [3, 4, 5, 12, 13, 14, 21, 22, 23], [6, 7, 8, 15, 16, 17, 24, 25, 26], [27, 28, 29, 36, 37, 38, 45, 46, 47],[30, 31, 32, 39, 40, 41, 48, 49, 50], [33, 34, 35, 42, 43, 44, 51, 52, 53], [54, 55, 56, 63, 64, 65, 72, 73, 74], [57, 58, 59, 66, 67, 68, 75, 76, 77], [60, 61, 62, 69, 70, 71, 78, 79, 80]]
   return lists
def initial_variables(puzzle, csp_table):
   csp = {}
   for x in range(len(puzzle)):
      csp[x] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
   for x in csp_table:
      for y in x:
         if puzzle[y]!=".":
            for z in x:
               if z!=y and puzzle[y] in csp[y]:
                  csp[y].remove(puzzle[y])
   return csp #instead of 9 for all, do it based on the puzzle
   
def main():
   puzzle = input("Type a 81-char string:") 
   while len(puzzle) != 81:
      print ("Invalid puzzle")
      puzzle = input("Type a 81-char string: ")
   csp_table = sudoku_csp()
   variables = initial_variables(puzzle, csp_table)
   print ("Initial:\n" + display(puzzle))
   solution = backtracking_search(puzzle, variables, csp_table)
   if solution != None: print ("solution\n" + display(solution))
   else: print ("No solution found.\n")
   
if __name__ == '__main__': main()

import sys; args = sys.argv[1:]
import re
dictwords = {}
allwords  = {}
startlist = []
def main():
   BLOCKCHAR = '#' # blocked square (black square)
   OPENCHAR = '-' # open square (not decided yet)
   PROTECTEDCHAR = '~' # Reserved for word characters
   print(args)
   board, width, height, words, blocks, txt = init(BLOCKCHAR, OPENCHAR, PROTECTEDCHAR)
   print("Initial: ")
   for i in words:
      h = int(i[1:i.find("x")])
      w = 0
      x = i.find("x")+1
      while(i[x].isdigit()):
         x+=1
         if x == len(i):
            break
      w = int(i[i.find("x")+1:x])
      length = len(i[x:])
      word = i[x:]
      if word == "":
         word = BLOCKCHAR
      if i[0]=="V" or i[0]=="v":
         for y in range(0,len(word)):
            board = board[:((y+h)*width+w)] + word[y].upper() + board[((y+h)*width+w)+1:]
      else:
         for x in range(0,len(word)):
            board = board[:(h*width+x+w)] + word[x].upper() +board[(h*width+x+w)+1:]   
   display(board, width, height)
   for i in range(0, len(board)):
      if board[i] == BLOCKCHAR:
            board = board[:len(board)-i-1] + BLOCKCHAR + board[len(board)-i:]
      if board[i] == PROTECTEDCHAR:
            board = board[:len(board)-i-1] + PROTECTEDCHAR + board[len(board)-i:]
   s = BLOCKCHAR*(width+2) ##fill border with BLOCKCHAR
   for i in range(0,height):
      s = s + BLOCKCHAR + board[i*width:(i+1)*width] + BLOCKCHAR
   s += BLOCKCHAR*(width+2)
   board = s
   width = width + 2
   height = height + 2
   substituteRegex = "[{}]{}(?=[{}])".format(BLOCKCHAR, OPENCHAR, BLOCKCHAR)
   subRE2 = "[{}]{}{}(?=[{}])".format(BLOCKCHAR, OPENCHAR, OPENCHAR, BLOCKCHAR)
   for counter in range(2):
      board = re.sub(substituteRegex, BLOCKCHAR*2, board)
      board = re.sub(subRE2, BLOCKCHAR*3, board) #helps checking by already filling in MUST fill values for this arrangement
      board = transpose(board, width)
      width = height
      height = len(board)//width
   s = ""
   width = width - 2
   height = height - 2
   for j in range(1,height+1):
      for i in range(1,width+1):
        s = s + board[j*(width+2)+i]
   board = s

   board = protect(board, width, height, BLOCKCHAR, OPENCHAR, PROTECTEDCHAR)
   board = placeBlock(board, width, height, blocks,BLOCKCHAR, OPENCHAR, PROTECTEDCHAR)
   if board != False:
      for i in range(0,len(board)):
         if board[i] == PROTECTEDCHAR:
            board = board[:i] + OPENCHAR + board[i+1:]
      for i in words:
         h = int(i[1:i.find("x")])
         w = 0
         x = i.find("x")+1
         while(i[x].isdigit()):
            x+=1
            if x ==len(i):
               break
         w = int(i[i.find("x")+1:x])
         length = len(i[x:])
         word = i[x:]
         if word == "":
            word = BLOCKCHAR
         if i[0]=="V" or i[0]=="v":
            for y in range(0,len(word)):
               board = board[:((y+h)*width+w)] + word[y].upper() + board[((y+h)*width+w)+1:]
         else:
            for x in range(0,len(word)):
               board = board[:(h*width+x+w)] + word[x].upper() +board[(h*width+x+w)+1:]   
      display(board, width, height)
   else:
      print("Could not create crossword board")
   f = open(txt, "r")
   for l in f:
         l = l.rstrip().upper()
         if len(l) not in allwords:
            allwords[len(l)] = set()
         allwords[len(l)].add(l)
         if len(l) not in dictwords:
            dictwords[len(l)] = {}
         for i in range(0,len(l)):
            if l[i] not in dictwords[len(l)]:
               dictwords[len(l)][l[i]] = {}
            if i not in dictwords[len(l)][l[i]]:
               dictwords[len(l)][l[i]][i] = set()
            dictwords[len(l)][l[i]][i].add(l)
            
   board = solve(guranteed_start_positions(board, height, width, dictwords, BLOCKCHAR, OPENCHAR, PROTECTEDCHAR), board, width, height, BLOCKCHAR, OPENCHAR)
   if board != False:
      display(board, width, height)
   else:
      print("Could not solve")
def solve(starts, board, width, height, BLOCKCHAR, OPENCHAR):
   global startlist
   for i in starts:
      startlist.append(i)
   board = recur(starts, board, width, height, OPENCHAR)
   return board
def complete(board, width, height, OPENCHAR):
   global startlist
   return board.count(OPENCHAR) == 0 and len(startlist)==0

def reorder(starts, board, width, height, OPENCHAR):
    global startlist
    list = []
    for i in startlist:
       words = allwords[len(i[2])]
       for y in range(0,len(i[2])):
             if board[i[0][y]]!=OPENCHAR:
                if board[i[0][y]] in dictwords[len(i[2])]:
                   if y in dictwords[len(i[2])][board[i[0][y]]]:
                      words = words.intersection(dictwords[len(i[2])][board[i[0][y]]][y])
                   else:
                     return False
                else: return False
       list.append((i, len(words)))
    list = sorted(list, key=lambda x: x[1])
    for i in range(0,len(list)):
       list[i] = list[i][0]
    startlist = list
    return True
def recur(starts, board, width, height, OPENCHAR):
   display(board, width, height)
   if complete(board, width, height, OPENCHAR): return board
   if not reorder(starts, board, width, height, OPENCHAR):
      return False
   global startlist
   value = startlist.pop(0)
   words = allwords[len(value[2])]
   for i in range(0,len(value[2])):
         if board[value[0][i]] != OPENCHAR:
            if board[value[0][i]] in dictwords[len(value[2])]:
               if i in dictwords[len(value[2])][board[value[0][i]]]:
                  words = words.intersection(dictwords[len(value[2])][board[value[0][i]]][i])
               else:
                  words = set()
            else: words = set()
   for word in words:
         #if valid(starts, value, word,board, width, height, OPENCHAR):
            #fill board with the new word
            xw = board
            allwords[len(value[2])].remove(word)
            for i in range(0,len(word)):
               board = board[:value[0][i]] + word[i].upper() + board[value[0][i]+1:]
            result = recur(starts, board, width, height, OPENCHAR)
            if result!=False:
               return result
            board = xw
            allwords[len(value[2])].add(word)
   #list = startlist
   startlist = [value]+ startlist
   return False

def guranteed_start_positions(board, height, width, all_words, BLOCKCHAR, OPENCHAR, PROTECTEDCHAR):
   xw = BLOCKCHAR*(width+3)
   xw += (BLOCKCHAR*2).join([board[p:p+width] for p in range(0, len(board), width)])
   xw += BLOCKCHAR*(width+3)
   pattern = r'[{}]({}|\w)*(?=[{}])'.format(BLOCKCHAR, OPENCHAR, BLOCKCHAR)
   regex = re.compile(pattern)
   width_turn = [width+2, height+2]
   pos_word_list = [] # In your own way, fill this list or other type of data structure.
   for turn in range(2):
      for m in regex.finditer(xw): # finditer(subject) after compile -> list of matches
         pos = 0
         word = xw[m.start()+1:m.end()]
         regex2 = re.compile('\\b' + word.replace(OPENCHAR, '\\w') + '\\b')
         if len(word)>0 and word.count(OPENCHAR) == 0 and turn == 0:
            pos = ((m.start()+1)//(width+2)-1)*width + (m.start()+1) % (width+2) -1
            pos_list = [p for p in range(pos, pos+len(word))]
            pos_word_list.append([pos_list, 'H', word.upper()])
         elif len(word)>0 and word.count(OPENCHAR) == 0 and turn == 1:
            pos = (((m.start()+1) % (height+2))-1)*width + (m.start()+1)//(height+2)-1
            pos_list = [pos + p*width for p in range(len(word))]
            pos_word_list.append([ pos_list, 'V', word.upper()])
         elif len(word)>0 and turn==0:
            candidates = all_words[len(word)]
            pos = ((m.start()+1)//(width+2)-1)*width + (m.start()+1) % (width+2) -1
            pos_list = [p for p in range(pos, pos+len(word))]
            pos_word_list.append([pos_list, 'H', word.upper()])
         elif len(word)>0 and turn == 1:
            candidates = all_words[len(word)]
            pos = (((m.start()+1) % (height+2))-1)*width + (m.start()+1)//(height+2)-1
            pos_list = [pos + p*width for p in range(len(word))]
            pos_word_list.append([pos_list, 'V', word.upper() ])
      xw = transpose(xw, width_turn[turn])
   for item in pos_word_list:
      num_of_o = item[2].count(OPENCHAR)
      #item.append(num_of_o)
      #print(item[3])
      # number of open-chars is also essential information
      # by working on with open-chars and letter-chars, you may update candidates
   return pos_word_list
   #num of candidates, list of positions, horizontal/vertical, word, possible candidates, number of open chars

def placeBlock(board, width, height, blocks, BLOCKCHAR, OPENCHAR, PROTECTEDCHAR):
   if blocks>0:
       if width%2==1 and height%2==1 and blocks%2==1:
           board = board[:len(board)//2] + BLOCKCHAR + board[1+len(board)//2:]
       #elif(width%2==1 and height%2==1 and blocks%2==0):
       #  board = board[:len(board)//2] + PROTECTEDCHAR + board[1+len(board)//2:]
       board = recursive_backtracking(board, generate_possibles(board, OPENCHAR), blocks, width, height, BLOCKCHAR, OPENCHAR, PROTECTEDCHAR)
   return board
            
def generate_possibles(board, OPENCHAR):
   list = []
   for i in range(0,len(board)):
      if board[i] == OPENCHAR:
         list.append(i)
   #random.shuffle(list)
   return list
def check_complete(board, width, height, blocks, BLOCKCHAR, OPENCHAR, PROTECTEDCHAR):
   return board.count(BLOCKCHAR)==blocks
   
def recursive_backtracking(board, variables, blocks, width, height, BLOCKCHAR, OPENCHAR, PROTECTEDCHAR):
   if check_complete(board, width, height, blocks, BLOCKCHAR, OPENCHAR, PROTECTEDCHAR): return board
   for value in variables:
      if isValid(value,board, width, height, blocks, BLOCKCHAR, OPENCHAR, PROTECTEDCHAR):
         board = board[:value] + BLOCKCHAR + board[value+1:]
         board = board[:len(board)-value-1] + BLOCKCHAR + board[len(board)-value:]
         result = recursive_backtracking(board, generate_possibles(board, OPENCHAR), blocks, width, height, BLOCKCHAR, OPENCHAR, PROTECTEDCHAR)
         if result!=False: return result
         board = board[:value] + OPENCHAR + board[value+1:]
         board = board[:len(board)-value-1] + OPENCHAR + board[len(board)-value:]
   return False

def isValid(value, board, width, height, blocks, BLOCKCHAR, OPENCHAR, PROTECTEDCHAR):
   board = board[:value] + BLOCKCHAR + board[value+1:]
   if board[len(board)-value-1] == PROTECTEDCHAR:
      return False 
   board = board[:len(board)-value-1] + BLOCKCHAR + board[len(board)-value:]
   display(board, width, height)
   s = BLOCKCHAR*(width+2) ##fill border with BLOCKCHAR
   for i in range(0,height):
      s = s + BLOCKCHAR + board[i*width:(i+1)*width] + BLOCKCHAR
   s += BLOCKCHAR*(width+2)
   board = s
   width = width + 2
   height = height + 2
   illegalRegex = "[{}](.?[{}]|[{}].?)[{}]".format(BLOCKCHAR, PROTECTEDCHAR,PROTECTEDCHAR, BLOCKCHAR) # have to seperate each regex into for loops in order to prevent interrows
   for j in range(0,height):
      s = board[j*width:(j+1)*width]
      if re.search(illegalRegex, s): 
         #print("3")
         return False #also have to do the transpose for this since we are just checking rows in regex and not columns
   board = transpose(board, width)
   width = height
   height = len(board)//width
   for j in range(0,height):
      s = board[j*width:(j+1)*width]
      if re.search(illegalRegex, s):
         #print("3")
         return False#also have to do the transpose for this since we are just checking rows in regex and not columns
   board = transpose(board, width)
   width = height
   height = len(board)//width
   substituteRegex = "[{}]{}(?=[{}])".format(BLOCKCHAR, OPENCHAR, BLOCKCHAR)
   subRE2 = "[{}]{}{}(?=[{}])".format(BLOCKCHAR, OPENCHAR, OPENCHAR, BLOCKCHAR)
   for counter in range(2):
      board = re.sub(substituteRegex, BLOCKCHAR*2, board)
      board = re.sub(subRE2, BLOCKCHAR*3, board) #helps checking by already filling in MUST fill values for this arrangement
      board = transpose(board, width)
      width = height
      height = len(board)//width
   s = ""
   width = width - 2
   height = height - 2
   for j in range(1,height+1):
      for i in range(1,width+1):
        s = s + board[j*(width+2)+i]
   board = s
   if blocks < board.count(BLOCKCHAR):
      #print("Too many blocks")
      return False
   
    #Probably want to also make the transposes 
    #AREA FILL:
    #start at any open char and make a set of indexes for open chars
    #flood by checking each top, left, right, and bottom and adding to the set
    #for each of those keep going
    #make sure to not check further if it's at a border 
    #when stopped compare set size to number of open chars in board (if same then it's not closed)
   visit = set()
   current = [] #keeps track of indexes currently looking at
   var = board.find(OPENCHAR)
   if var == -1:
      var = board.find(PROTECTEDCHAR)
   current.append(var)
   while(len(current)!=0):
      var = current.pop(0)
      if var>=width:
         if (board[var-width]==OPENCHAR or board[var-width]==PROTECTEDCHAR) and (var-width) not in visit:
            current.append(var-width)
            visit.add(var-width)
      if var%width!=0:
         if (board[var-1] == OPENCHAR or board[var-1] == PROTECTEDCHAR) and (var-1) not in visit:
            current.append(var-1)
            visit.add(var-1)
      if (var+1)%width!=0:
         if (board[var+1] == OPENCHAR or board[var+1] == PROTECTEDCHAR) and (var+1) not in visit:
            current.append(var+1)
            visit.add(var+1)
      if var<(height-1)*width:
         if (board[var+width]==OPENCHAR or board[var+width]==PROTECTEDCHAR) and (var+width) not in visit:
            current.append(var+width)
            visit.add(var+width)
   if len(visit)!=board.count(OPENCHAR)+board.count(PROTECTEDCHAR):
     #print("not open")
     return False
   display(board, width, height) 
   return True
    #ENDS WHEN current has no more
    #reset without the borders of #:
   
def transpose(board, width):
   return "".join([board[col::width] for col in range(width)])

def protect(board, width, height, BLOCKCHAR, OPENCHAR, PROTECTEDCHAR):
   for i in range(0, width*height):
      if board[i] != OPENCHAR and board[i]!=BLOCKCHAR:
         board = board[:i] + PROTECTEDCHAR + board[i+1:]
   for i in range(0, width*height):
      if board[i] == PROTECTEDCHAR:
         #horizontal
         if (i%width==0):
            if(board[i+1] !=BLOCKCHAR and board[i+2] !=BLOCKCHAR):
               board = board[:i+1] + PROTECTEDCHAR+PROTECTEDCHAR+board[i+3:]
         elif((i+1)%width==0):
            if(board[i-1] !=BLOCKCHAR and board[i-2] !=BLOCKCHAR):
               board = board[:i-2] + PROTECTEDCHAR + PROTECTEDCHAR + board[i:]
         elif((i+2)%width==0):
            if((board[i-1]!=PROTECTEDCHAR or board[i+1]!=PROTECTEDCHAR)and(board[i-1]!=PROTECTEDCHAR or board[i-2]!=PROTECTEDCHAR)):
               if board[i-1]!=BLOCKCHAR and board[i+1]!=BLOCKCHAR:
                  board = board[:i-1] + PROTECTEDCHAR +board[i]+ PROTECTEDCHAR + board[i+2:]
               elif (board[i-1] !=BLOCKCHAR and board[i-2] !=BLOCKCHAR):
                  board = board[:i-2] + PROTECTEDCHAR + PROTECTEDCHAR + board[i:]
         elif((i-1)%width==0):
            if((board[i-1]!=PROTECTEDCHAR or board[i+1]!=PROTECTEDCHAR)and(board[i+1]!=PROTECTEDCHAR or board[i+2]!=PROTECTEDCHAR)):
               if board[i-1]!=BLOCKCHAR and board[i+1]!=BLOCKCHAR:
                  board = board[:i-1] + PROTECTEDCHAR +board[i]+ PROTECTEDCHAR + board[i+2:]
               elif board[i+1]!=BLOCKCHAR and board[i+2]!=BLOCKCHAR:
                  board = board[:i+1] + PROTECTEDCHAR+PROTECTEDCHAR+board[i+3:]  
         else:
            if((board[i-1]!=PROTECTEDCHAR or board[i+1]!=PROTECTEDCHAR)and(board[i-1]!=PROTECTEDCHAR or board[i-2]!=PROTECTEDCHAR)and(board[i+1]!=PROTECTEDCHAR or board[i+2]!=PROTECTEDCHAR)):
               if(i>(width/2)):
                  if board[i+1]!=BLOCKCHAR and board[i+2]!=BLOCKCHAR:
                     board = board[:i+1] + PROTECTEDCHAR+PROTECTEDCHAR+board[i+3:]
                  elif board[i-1]!=BLOCKCHAR and board[i+1]!=BLOCKCHAR:
                     board = board[:i-1] + PROTECTEDCHAR +board[i]+ PROTECTEDCHAR + board[i+2:]
                  elif board[i-1] !=BLOCKCHAR and board[i-2] !=BLOCKCHAR:
                     board = board[:i-2] + PROTECTEDCHAR + PROTECTEDCHAR + board[i:]
               else:
                  if board[i-1] !=BLOCKCHAR and board[i-2] !=BLOCKCHAR:
                     board = board[:i-2] + PROTECTEDCHAR + PROTECTEDCHAR + board[i:]
                  elif board[i-1]!=BLOCKCHAR and board[i+1]!=BLOCKCHAR:
                     board = board[:i-1] + PROTECTEDCHAR +board[i]+ PROTECTEDCHAR + board[i+2:]
                  elif board[i+1]!=BLOCKCHAR and board[i+2]!=BLOCKCHAR:
                     board = board[:i+1] + PROTECTEDCHAR+PROTECTEDCHAR+board[i+3:]
         #vertical
         if (i<width):
            if (board[i+width]!=BLOCKCHAR and board[i+2*width]!=BLOCKCHAR):
               board = board[:i+width] + PROTECTEDCHAR + board[i+width+1:i+width*2] + PROTECTEDCHAR + board[i+width*2+1:]
         elif(i<2*width):
            if (board[i+width]!=PROTECTEDCHAR or board[i+2*width]!=PROTECTEDCHAR) and (board[i+width]!=PROTECTEDCHAR or board[i-1*width]!=PROTECTEDCHAR):
               if board[i+width]!=BLOCKCHAR and board[i-1*width]!=BLOCKCHAR:
                  board = board[:i-width] + PROTECTEDCHAR + board[i-width+1:i+width] + PROTECTEDCHAR + board[i+width+1:]
               elif board[i+width]!=BLOCKCHAR and board[i+2*width]!=BLOCKCHAR:
                  board = board[:i+width] + PROTECTEDCHAR + board[i+width+1:i+width*2] + PROTECTEDCHAR + board[i+width*2+1:]
         elif(i>=(width)*(height-1)):
            if (board[i-width]!=BLOCKCHAR and board[i-2*width]!=BLOCKCHAR):
               board = board[:i-2*width] + PROTECTEDCHAR + board[i-2*width+1:i-width] + PROTECTEDCHAR + board[i-width+1:]
         elif(i>=(width)*(height-2)):
            if (board[i-width]!=PROTECTEDCHAR or board[i-2*width]!=PROTECTEDCHAR) and (board[i+width]!=PROTECTEDCHAR or board[i-1*width]!=PROTECTEDCHAR):
               if board[i+width]!=BLOCKCHAR and board[i-1*width]!=BLOCKCHAR:
                  board = board[:i-width] + PROTECTEDCHAR + board[i-width+1:i+width] + PROTECTEDCHAR + board[i+width+1:]
               elif (board[i-width]!=BLOCKCHAR and board[i-2*width]!=BLOCKCHAR):
                  board = board[:i-2*width] + PROTECTEDCHAR + board[i-2*width+1:i-width] + PROTECTEDCHAR + board[i-width+1:]
         else:
            if (board[i-width]!=PROTECTEDCHAR or board[i-2*width]!=PROTECTEDCHAR) and (board[i+width]!=PROTECTEDCHAR or board[i-1*width]!=PROTECTEDCHAR) and (board[i+width]!=PROTECTEDCHAR or board[i+2*width]!=PROTECTEDCHAR):
               if(i>=(height/2)*width):
                  if board[i+width]!=BLOCKCHAR and board[i+2*width]!=BLOCKCHAR:
                     board = board[:i+width] + PROTECTEDCHAR + board[i+width+1:i+width*2] + PROTECTEDCHAR + board[i+width*2+1:]
                  elif board[i+width]!=BLOCKCHAR and board[i-1*width]!=BLOCKCHAR:
                     board = board[:i-width] + PROTECTEDCHAR + board[i-width+1:i+width] + PROTECTEDCHAR + board[i+width+1:]
                  elif (board[i-width]!=BLOCKCHAR and board[i-2*width]!=BLOCKCHAR):
                     board = board[:i-2*width] + PROTECTEDCHAR + board[i-2*width+1:i-width] + PROTECTEDCHAR + board[i-width+1:]
               else:
                  if (board[i-width]!=BLOCKCHAR and board[i-2*width]!=BLOCKCHAR):
                     board = board[:i-2*width] + PROTECTEDCHAR + board[i-2*width+1:i-width] + PROTECTEDCHAR + board[i-width+1:]
                  elif board[i+width]!=BLOCKCHAR and board[i-1*width]!=BLOCKCHAR:
                     board = board[:i-width] + PROTECTEDCHAR + board[i-width+1:i+width] + PROTECTEDCHAR + board[i+width+1:]
                  elif board[i+width]!=BLOCKCHAR and board[i+2*width]!=BLOCKCHAR:
                     board = board[:i+width] + PROTECTEDCHAR + board[i+width+1:i+width*2] + PROTECTEDCHAR + board[i+width*2+1:]

   display(board, width, height)
   return board
   
def display(board, width, height):
   s = ""
   for j in range(0,height):
      for i in range(0, width):
         s +=(board[j*width+i].upper())   
      s+="\n"
   print(s)
def init(BLOCKCHAR, OPENCHAR, PROTECTEDCHAR):
   board = ""
   width = 0
   height = 0
   words = []
   blocks = 0
   txt = ""
   intTest = [r"^(\d+)x(\d+)$", r"^\d+$", r"^(H|V)(\d+)x(\d+)(.*)$"]
   for i in args:
      match = re.search(intTest[0], i, re.I)
      if match!=None:
         height = int(match.group(1))
         width = int(match.group(2))
      match = re.search(intTest[1], i, re.I)
      if match!=None:
         blocks = int(match.group(0))
      match = re.search(intTest[2], i, re.I)
      if match!=None:
         words.append(match.group(0))
      match = re.search("^.*\.txt$", i, re.I)
      if match!=None:
         txt = match.group(0)
   for i in range(0,width):
      for j in range(0, height):
         board += OPENCHAR
   return board, width, height, words, blocks, txt
if __name__ =='__main__':
   main()
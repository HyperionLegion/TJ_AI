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
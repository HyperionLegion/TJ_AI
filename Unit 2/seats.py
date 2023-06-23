
def main():
   solved = set()
   s = "............"
   for i in range(0,len(s)):
      for j in range(0,len(s)):
         for x in range(0,len(s)):
            for y in range(0,len(s)):
               for z in range(0,len(s)):
                  if i==j or i==x or i==y or j==x or j==y or x==y or i==z or j==z or x==z or y==z:
                     s=s
                  else:
                        list = [i, j, x, y, z]
                        list.sort()
                        t = s[0:list[0]] + "1" + s[list[0]+1:list[1]] + "1" + s[list[1]+1:list[2]] + "1" + s[list[2]+1:list[3]] + "1" + s[list[3]+1:list[4]] + "1" + s[list[4]:]
                        distances = []
                        unique = True
                        for a in range(len(t)):
                           for b in range(a+1,len(t)):
                                 if t[a]=="1" and t[b]=="1":
                                    dist = abs(b-a)
                                    if dist in distances:
                                       unique=False
                                    else:
                                       distances.append(dist)
                        if(unique):
                          solved.add(t)
   
   print(len(solved))
   print(solved)
if __name__ == '__main__':
   main()
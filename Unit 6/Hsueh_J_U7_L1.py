import PIL
import random
import math
from PIL import Image
import urllib.request
import io, sys, os, random

def main():
   k = int(sys.argv[1])
   file = sys.argv[2]
   if not os.path.isfile(file):
      file = io.BytesIO(urllib.request.urlopen(file).read())
   img = Image.open(file)   
   width = img.size[0]
   height = img.size[1]
   unique = set()
   pix = img.load()
   pixels = {}
   max = 0
   maxi =0 
   maxj = 0
   for i in range(0,width):
      for j in range(0,height):
          unique.add(pix[i,j])
          if pix[i, j] not in pixels:
            pixels[pix[i, j]] = 0
          pixels[pix[i,j]] = pixels[pix[i, j]]+1
          if(pixels[pix[i,j]]>max):
            max = pixels[pix[i,j]]
            maxi = i
            maxj = j 
   #img.show()
   means = [pix[random.randint(0,width-1),random.randint(0,height-1)] for i in range(0,k)]
   #means = [(random.randint(0,255), random.randint(0,255),random.randint(0,255)) for i in range(0,k)]
   done = False
   clustered = [[0 for j in range(0,height)] for i in range(0,width)]
   #print(clustered)
   start = []
   old = []
   first = True
   diffc = 1
   print("Size: ", width, " x ", height)
   print("Pixels: ", width*height)
   print("Distinct pixel count: ", len(unique))
   print("Most common pixel: ", pix[maxi, maxj], max)
   print("Random means: ", means)
   for i in range(0,len(means)):
      start.append(0)
   while(not done):
      done = True
      old = [start[i] for i in range(0,len(means))]
      oldcluster = [[clustered[i][j] for j in range(0, height)] for i in range(0,width)]
      for i in range(0,len(means)):
         start[i]=0
      for i in range(0,width):
         for j in range(0,height):
            cluster = 0
            mindist = math.sqrt( pow(means[0][0]-pix[i,j][0], 2) + pow(means[0][1]-pix[i,j][1], 2) + pow(means[0][2]-pix[i,j][2], 2))
            for y in range(1,len(means)):
               if(math.sqrt( pow(means[y][0]-pix[i,j][0], 2) + pow(means[y][1]-pix[i,j][1], 2) + pow(means[y][2]-pix[i,j][2], 2)) < mindist):
                  cluster = y
                  mindist = math.sqrt( pow(means[y][0]-pix[i,j][0], 2) + pow(means[y][1]-pix[i,j][1], 2) + pow(means[y][2]-pix[i,j][2], 2))
            clustered[i][j] = cluster
            start[cluster] = start[cluster]+1
            if (cluster != oldcluster[i][j]):
               done = False
      for i in range(0,len(means)):
         r = 0
         g=0
         b=0
         count = 0
         for x in range(0, width):
            for y in range(0,height):
               if(clustered[x][y]==i):
                  count = count + 1
                  r = r + pix[x, y][0]
                  g = g + pix[x, y][1]
                  b = b + pix[x, y][2]
         if count > 0:
            means[i] = (r/count, g/count, b/count)
      if first:
         print("first means:", means)
         print("starting sizes:", start)
         first = False
      diffc = diffc + 1
      diff = [start[i] - old[i] for i in range(0,len(means))]
      print("diff ", diffc, " : ", diff)
      
   for i in range(0, width):
      for j in range(0, height):
         pix[i, j] = (int(means[clustered[i][j]][0]), int(means[clustered[i][j]][1]),int(means[clustered[i][j]][2]))
   img.show()
   img.save('./kmeans/2022jhsueh.png', 'PNG')
   print("Final sizes: ", start)
   print("Final means: ")
   for i in range(0, len(means)):
      print(str(i) + ": ", means[i], start[i])
      
if __name__ == '__main__': 
   main()
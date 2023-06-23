import PIL
from PIL import Image
import urllib.request
import io, sys, os, random

def main():
   URL = 'http://www.w3schools.com/css/trolltunga.jpg'
   f = io.BytesIO(urllib.request.urlopen(URL).read())
   img = Image.open(f)
   width = img.size[0]
   height = img.size[1]
   img.show()
   pix = img.load()
   for i in range(0,width):
      for j in range(0,height):
         if(pix[i,j][0]<=255//3):
            pix[i,j] = (0, pix[i,j][1], pix[i,j][2])
         elif (pix[i,j][0]>=255*2//3):
            pix[i,j] = (255, pix[i,j][1], pix[i,j][2])
         else:
            pix[i,j] = (127, pix[i,j][1], pix[i,j][2])
         if(pix[i,j][1]<=255//3):
            pix[i,j] = (pix[i,j][0], 0, pix[i,j][2])
         elif (pix[i,j][1]>=255*2//3):
            pix[i,j] = (pix[i,j][0], 255, pix[i,j][2])
         else:
            pix[i,j] = (pix[i,j][0], 127, pix[i,j][2])
         if(pix[i,j][2]<=255//3):
            pix[i,j] = (pix[i,j][0], pix[i,j][1], 0)
         elif (pix[i,j][2]>=255*2//3):
            pix[i,j] = (pix[i,j][0], pix[i,j][1], 255)
         else:
            pix[i,j] = (pix[i,j][0], pix[i,j][1], 127)
   img.show() 
if __name__ == '__main__': 
   main()
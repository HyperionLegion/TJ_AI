import os

water = 0
food = 0
wood = 0
waterbottle = 3

def clear(): 
  os.system('clear')


def choiceOne():
  global water
  Choice1 = input("Would you like to look for water, or find shelter(water/shelter): ")
  if Choice1 == "water":
      print("\nWhile looking around for water, you found a stream, you had some water bottles from the crash site, so you filled up 3 water bottles.\n")
      water = water + 1
  elif Choice1 == "shelter":
      print("\nWhile searching for shelter, you find an abandoned town and in the town you find some supplies, 3 peices of wood, and 2 more water bottles. \n")
  else:
    print("\nPlease Chose either water or shelter\n")
    choiceOne()
  return choiceOne
 
def printResource():
  print("Resources")
  print("water = ",water)
  print("food = ",food)
  print("wood = ",wood)
  print("waterbottles = ",waterbottle)



#**main***.
print("You were flying through the clouds when all of a sudden you started rapidly falling out of the sky so you had to do an emergancy crash, landing in the middle of a jungle.\n")
choiceOne()
printResource()
input("\nPress Enter to continue...")
clear()
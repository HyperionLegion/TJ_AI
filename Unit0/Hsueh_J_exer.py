# Name: Joshua Hsueh
# Date: 9/10/2020
# Do not forget to change the file name -> Save as

''' Tasks '''
# 1. Given an input of a space-separated list of any length of integers, output the sum of them.
# 2. Output the list of those integers (from #1) that are divisible by three.
s = input("list of numbers: ").strip().split() 
print ("1. sum = ", sum([int(x) for x in s]))
print ("2. list of multiples of 3: ", [int(x) for x in s if int(x) % 3 == 0])



# 3. Given an integer input, print the first n Fibonacci numbers. eg. n=6: 1, 1, 2, 3, 5, 8
f1, f2,s, =1, 1, input("Type n for Fibonacci sequence: ").strip()
print("3. fibonnaci:", end= " ")
for x in range(0,int(s)):
   print(str(f1), end=" ")
   next = f1+f2
   f1=f2
   f2=next
print()
# 4. Given an input, output a string composed of every other character. eg. Aardvark -> Arvr
print("4. every other str: ", input("Type a string: ").strip()[::2])


# 5. Given a positive integer input, check whether the number is prime or not.
a = int(input("Type a number to check prime: ").strip())
if a == 0 or a==1:
   print("5. Is Prime? False.")
else:
   for i in range (2, a-1): 
      if a%i==0: print("5. Is Prime? False."); break;
   else:   print("5. Is Prime? True.")
# 6. Calculate the area of a triangle given three side lengths.  eg. 13 14 15 -> 84
s = input("Type three sides of a triangle: ").strip().split()
a, b, c = int(s[0]), int(s[1]), int(s[2])
p = (a + b + c)/2
print("6. The area of "+str(a)+" "+str(b)+" "+str(c)+" is " + str((p*(p-a)*(p-b)*(p-c))**0.5))
# 7. Given a input of a string, remove all punctuation from the string. 
# eg. "Don't quote me," she said. -> Dontquotemeshesaid
s = input("Type a sentence: ")
print("7. Punct removed: ", s.strip().replace(' ', '').replace(',', '').replace('.', '').replace('"', '').replace('\'', '').replace('!', '').replace('?','').replace('-',''))
# 8. Check whether the input string (from #7, lower cased, with punctuation removed) is a palindrome.
a = s.strip().replace(' ', '').replace(',', '').replace('.', '').replace('"', '').replace('\'', '').replace('!','').replace('?','').replace('-','')
print("8. Is palindrome? True." if a.lower()==a[::-1].lower() else "8. Is palindrome? False.")
# 9. Count the number of each vowel in the input string (from #7).
print("9. Count each vowel: "+str({'a':a.count('a'), 'e':a.count('e'), 'i':a.count('i'), 'o':a.count('o'), 'u':a.count('u')}))

#lower?^^
 
# 10. Given two integers as input, print the value of f\left(k\right)=k^2-3k+2 for each integer between the two inputs.  
# eg. 2 5 -> 0, 2, 6, 12
s = input("Type two integers (lower bound and upper bound): ").strip().split()
a, b = int(s[0]), int(s[1])
print("10. Evalute f(k)=k^2-3k+2 from "+str(a)+" to "+str(b)+":"," ".join(str(x**2-3*x+2 ) for x in range (a, b+1)))
# 11. Given an input of a string, determines a character with the most number of occurrences.
dict, maxes, s = {}, set(), input("Type a string: ").strip()
for i in s: 
   dict[i]=(1 if i not in dict else dict[i]+1)
for i in s:
   maxes.add(i if s.count(i)==s.count(max(dict, key=dict.get))else None)
print("11. Most occured char:", " ".join(i for i in maxes if i!=None))
# 12. With the input string from #11, output a list of all the words that start and end in a vowel.
print("12. List of words starting and ending with vowels:", str([i for i in s.split() if i[0] in "aeiou"]))
# 13. With the input string from #11, capitalizes the starting letter of every word of the string and print it.
print("13. Capitalize starting letter for every word:", " ".join(i.title() for i in s.split()))
# 14. With the input string from #11, prints out the string with each word in the string reversed.
print("14. Reverse every word:", " ".join(i[::-1] for i in s.split()))

# 15. With the input string from #11, treats the first word of the input as a search string to be found in the rest 
# of the string, treats the second word as a replacement for the first, and treats the rest of the input as the string to be searched.
# 	eg.    b Ba baby boy ->  BaaBay Baoy
print("15. Find the first and replace with the second:", " ".join(i.replace(s.split()[0], s.split()[1]) for i in s.split()[2:]))


 
# 16. With an input of a string, removes all duplicate characters from a string.  Eg. detection -> detcion
s = input("Type a string to remove all duplicate chars: ").strip()
print("16. Remove all duplicat chars:", "".join(s[index]for index in range(0,len(s)) if s[index] not in s[:index]))
# 17. Given an input of a string, determines whether the string contains only digits.
s = input("Type a string to check if it has only digits or not: ").strip()
print("17. Is a number?: "+ str(s.isdigit()))
# 18. If #17 prints True, determines whether the string contains only 0 and 1 characters, and if so assumes it is a binary string, 
print("18. It is a binary number: "+ str(int(s, 2)) if s.count('0')+s.count('1')==len(s) else "18. It is not a binary number")
# converts it to a number, and prints out the decimal value.


 
# 19. Write a script that accepts two strings as input and determines whether the two strings are anagrams of each other.
s, a = input("Type the first string to check anagram: ").strip(), input("Type the second string to check anagram: ").strip() 
print("19. Are " + s+" and "+a+ " anagrams?: "+ str(sorted(s)==sorted(a)))


# 20. Given an input filename, if the file exists and is an image, find the dimensions of the image.
import PIL, io, sys
from PIL import Image
s = input("Type the image file name: ").strip()
print("20. Image dimension:", str(Image.open(s).width) + " by " + str(Image.open(s).height))
#53633606_359268751593903_6794998339445194752_o.jpg

# 21. Given an input of a string, find the longest palindrome within the string.
s, longest = input("Type a string to find the longest palindrome: ").strip().replace(' ',''), s[0]
for x in range(len(s)+1):
    for y in range(len(s)+1):
        longest = s[y:x+y] if s[y:x+y] == s[y:x+y][::-1] and len(s[y:x+y]) > len(longest) else longest
print("21. Longest palindrome within the string:", longest)

# 22. Given an input of a string, find all the permutations of a string.
s, perms= input("Type a string to do permutation: ").strip().replace(' ',''), []
perms.append(s[0])
for x in range(1, len(s)):
   for y in reversed(range(len(perms))):
      a = perms.pop(y)
      for z in range(len(a)+1):
         perms.append(a[:z]+s[x]+a[z:])
print("22. all permutations: " + str(perms))
# 23. Given the input string from #22, find all the unique permutations of a string.
print("23. all unique permutations:", str(set(perms)))
 
# 24. Given an input of a string, find a longest non-decreasing subsequence within the string (according to ascii value).
s = input("Type a string to find the longest non-decreasing sub: ").strip().replace(' ','')
longest = ""+s[0]
for x in range(0,len(s)):
   i = x+1;
   while i<len(s) and ord(s[i])>=ord(s[i-1]):
      longest = s[x:i+1] if len(longest)<len(s[x:i+1]) else longest
      i+=1
print("24. longest non-decreasing sub:", longest)
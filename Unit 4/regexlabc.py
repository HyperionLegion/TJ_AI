# Nicole Kim, 2/14/2021
import re

'''In Q50-52, do not use lookarounds'''

def num_50(subject):
   # Match all words where some letter appears two or more times in the same word. 
   # Sample input subject: Nobody can make you feel inferior without your permission
   # Sample output: ['Nobody', 'feel', 'inferior', 'without', 'permission']
   pattern = r"\b\w*(\w)\w*\1\w*"  # fix this!! 
   regex = re.compile(pattern, re.I)
   print ([subject[m.start():m.end()] for m in regex.finditer(subject)])

def num_51(subject):
   # Match all words where some letter appears four times in the same word.
   # Smaple input subject: We had an assessment about Peewee.
   # Sample output: ['assessment', 'Peewee']
   pattern = r"\b\w*((\w)(\w*\2){3})\w*"
   regex = re.compile(pattern, re.I)
   print ([subject[m.start():m.end()] for m in regex.finditer(subject)])

def num_52(subject):
   # Match on all non-empty binary strings with the same number of 01 substrings as 10 substrings.
   # Sample input subject: 100110101
   # Sample output: 100110101
   pattern = r"^0[01]*0$|^1[01]*1$"
   match = re.match(pattern, subject)
   print (match.group(0)) if match != None else print (match)

def num_53(subject):
   # Match all six letter words containing the substring cat.
   # Sample input subject: Two Caties lose some cattle every year.
   # Sample output: ['Caties', 'cattle']
   pattern = r"\b(?=\w*cat)\w{6}\b"
   print (re.findall(pattern, subject, re.I))

def num_54(subject):
   # Match all 5 to 9 letter words containing both the substrings bri and ing.
   # Sample intput subject: Bridget didn't bring anything formal for brightening
   # Sample output: ['bring']
   pattern = r"\b(?=\w*bri)(?=\w*ing)\w{5,9}\b"
   print (re.findall(pattern, subject, re.I))

def num_55(subject):
   # Match all six letter words not containing the substring cat.
   # Sample input subject: Two Caties bought some cattle every year at the cattle market
   # Sample output: ['bought', 'market']
   pattern = r"\b(?!\w*cat)\w{6}\b"
   regex = re.compile(pattern, re.I)
   print ([subject[m.start():m.end()] for m in regex.finditer(subject)])

def num_56(subject):
   # Match all words with no repeated characters.
   # Sample input subject: Nobody can make you feel inferior without your permission
   # Sample output: ['can', 'make', 'you', 'your']
   pattern = r"\b(?!\w*(\w)\w*\1)\w+"
   regex = re.compile(pattern, re.I)
   print ([subject[m.start():m.end()] for m in regex.finditer(subject)])

def num_57(subject):
   # Match on all binary strings not containing the forbidden substring 10011.
   # Sample input subject: 10110110
   # Sample output: 10110110
   pattern = r"^(?!.*10011)[10]*$"
   match = re.match(pattern, subject)
   print (match.group(0)) if match != None else print (match)

def num_58(subject):
   # Match all words having two different adjacent vowels.
   # Sample input subject: Nobody can make you feel inferior without your permission
   # Sample output: ['you', 'inferior', 'without', 'your', 'permission']
   pattern = r"\b\w*([aeiou])(?!\1)[aeiou]\w*"
   regex = re.compile(pattern, re.I)
   print ([subject[m.start():m.end()] for m in regex.finditer(subject)])

def num_59(subject):
   # Match on all binary strings containing neither 101 nor 111 as substrings. 
   # Sample input subject: 100000010
   # Sample output: 100000010
   pattern = r"^(?!.*(101)|(111))[10]*$"
   match = re.match(pattern, subject)
   print (match.group(0)) if match != None else print (match)

def num_60(subject):
   # Match on all binary strings containing neither 101 nor 111 as substrings. 
   # Sample input subject: 100000010
   # Sample output: 100000010
   pattern = r"^^0{0,2}(1+0{0,2})*$"
   match = re.match(pattern, subject)
   print (match.group(0)) if match != None else print (match)

while(True):
   input_num = input("Choose the exercise # (50 - 59 or -1 to terminate):")
   if input_num == '-1': exit("Good bye")
   input_str = input("Input subject: ")
   eval("num_"+input_num)(input_str)
   print()
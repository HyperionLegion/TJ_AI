#Joshua Hsueh
#9/8/2020

def sleep_in(weekday, vacation):
   return not weekday or vacation
   
def monkey_trouble(a_smile, b_smile):
   return a_smile == b_smile
   
def sum_double(a, b):
  return 2 * ( a + b) if a == b else a + b

def diff21(n):
  return (21-n if n<=21 else 2*(n-21))

def parrot_trouble(talking, hour):
  return (True if talking and (hour<7 or hour>20) else False)  

def makes10(a, b):
  return True if a + b == 10 or a==10 or b==10 else False

def near_hundred(n):
  return (True if (abs(100-n)<=10 or abs(200-n)<=10) else False)

def pos_neg(a, b, negative):
  return (True if a < 0 and b < 0 else False) if negative else (True if (a>0 and b<0) or (a<0 and b>0) else False)

def hello_name(name):
  return 'Hello ' + name+'!'

def make_abba(a, b):
  return a + b +  b + a

def make_tags(tag, word):
  return '<'+tag+'>'+word+'</'+tag+'>'

def make_out_word(out, word):#): fatal error
  return out[:int(len(out)/2)] + word + out[int(len(out)/2):]

def extra_end(str):
  return str[len(str)-2:]*3

def first_two(str):
  return str if len(str)<2 else str[:2]

def first_half(str):
  return str[:int(len(str)/2)]

def without_end(str):
  return str[1:-1]

def first_last6(nums):
  return True if 6==nums[0] or 6 == nums[-1] else False
  
def same_first_last(nums):
  return (True if nums[0]==nums[-1] else False) if len(nums)>=1 else False

def make_pi(n):
  return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7][0:n]

def common_end(a, b):
  return True if a[0]==b[0] or a[-1]==b[-1] else False

def sum3(nums):
  return sum(i for i in nums)

def rotate_left3(nums):
  return nums[1:] + (nums[:1])

def reverse3(nums):
  return nums[::-1]
  
def max_end3(nums):
  return [nums[0]]*len(nums) if nums[0]>nums[-1] else [nums[-1]]*len(nums)


def cigar_party(cigars, is_weekend):
  return (True if cigars>=40 else False) if is_weekend else (True if cigars<=60 and cigars>=40 else False)

def date_fashion(you, date):
  return 0 if you<=2 or date<=2 else (2 if you>=8 or date>=8 else 1)

def squirrel_play(temp, is_summer):
  return (True if temp>=60 and temp<=100 else False) if is_summer else (True if temp>=60 and temp<=90 else False)

def caught_speeding(speed, is_birthday):
  return (0 if speed <= 65 else (1 if speed>=66 and speed<=85 else 2)) if is_birthday else (0 if speed <= 60 else (1 if speed>=61 and speed<=80 else 2))

def sorta_sum(a, b):
  return 20 if a + b >=10 and a + b <=19 else a + b

def alarm_clock(day, vacation):
  return ('10:00' if day>=1 and day<=5 else 'off')if vacation else ('7:00'if day>=1 and day<=5 else '10:00')

def love6(a, b):
  return True if a==6 or b==6 or abs(a-b)==6 or a+b==6 else False

def in1to10(n, outside_mode):
  return (True if n<=1 or n>=10 else False) if outside_mode else (True if n>=1 and n<=10 else False)


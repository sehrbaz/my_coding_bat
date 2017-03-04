#Warmup-1 > sleep_in
####
def sleep_in(weekday, vacation):
  return vacation or not weekday

#Warmup-1 > monkey_trouble
####
def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

#Warmup-1 > sum_double
####
def sum_double(a, b):
  if a == b:
    return (a + b) *2
  else: return (a + b)

#Warmup-1 > diff21
####
def diff21(n):
  if n > 21:
    return (21 - n) * (-2)
  else: return (21 - n)

#Warmup-1 > parrot_trouble
####
def parrot_trouble(talking, hour):
  return talking and not (7 <= hour <= 20)

#Warmup-1 > makes10
####
def makes10(a, b):
  return (a == 10 or b == 10 or a + b == 10)

#Warmup-1 > near_hundred
###
def near_hundred(n):
  return (abs(n - 100) <= 10 or abs(n - 200) <= 10)

#Warmup-1 > pos_neg
###
def pos_neg(a, b, negative):
  if a < 0 and b < 0:
    return negative
  elif a > 0 and b > 0:
    return False
  else: return not negative
#  or
def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return (a < 0 and b > 0) or (a > 0 and b < 0)

#Warmup-1 > not_string
def not_string(str):
    if str[:3] <> "not":
        return "not " + str
    else:
        return str
#Warmup-1 > missing_char
def missing_char(str, n):
    return str[:n] + str[n+1:]
#alternative
def missing_char(str, n):
  return str.replace(str[n], ''

#Warmup-1 > front_back
def front_back(str):
  n = len(str)
  if n > 1:
    return str[n-1] + str[1:n-1] + str[0]
  else: return str

#Warmup-1 > front3
def front3(str):
    return 3 * str[:3]

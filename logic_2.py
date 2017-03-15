#CodingBat Python practice problems
# Logic-2

#Logic-2 > make_bricks
def make_bricks(small, big, goal):
    return goal%5 <= small  and small + 5 * big >= goal

#Logic-2 > lone_sum
def lone_sum(a, b, c):
    if a == b == c:
      return 0
    elif a == b and b != c:
      return c
    elif a != b and b == c:
      return a
    elif a == c and a != b:
      return b
    else:
      return a + b + c
#alternative unfortuntekly not my solution =)
def lone_sum(a, b, c):
    sum = 0
    if a != b and a != c: sum += a
    if b != a and b != c: sum += b
    if c !+ a and c != b: sum += c
    return sum

#Logic-2 > lucky_sum
def lucky_sum(a, b, c):
    sum = 0
    if a != 13:
      sum += a
      if b != 13:
        sum += b
        if c != 13:
          sum += c
    return sum

#Logic-2 > no_teen_sum
def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n in [13, 14, 17, 18, 19]:
      return 0
    return n

#Logic-2 > round_sum
def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(num):
    if num % 10 >= 5:
      num = (num // 10 + 1) * 10
    else:
      return num - (num % 10)
    return num

#Logic-2 > close_far
def close_far(a, b, c):
    return (abs(a-b) <= 1 and abs(a-c) >=2 and abs(c-b)>= 2) or (abs(a-c) <= 1 and abs(a-b) >=2 and abs(c-b)>= 2)

#Logic-2 > make_chocolate
def make_chocolate(small, big, goal):
    if goal % 5 <= small and small + 5 * big >= goal:
      if goal // 5 >= big:
        return goal - big * 5
      elif goal // 5 < big:
        return goal % 5
    else:
      return -1

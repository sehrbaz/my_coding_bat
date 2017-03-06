#CodingBat Python practice problems
# Logic-1

# Logic-1 > cigar_party 
def cigar_party(cigars, is_weekend):
    return ((40 <= cigars <= 60)) or (((cigars >= 40) and is_weekend))

#Logic-1 > date_fashion 
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1

#Logic-1 > squirrel_play 
def squirrel_play(temp, is_summer):
    return (60 <= temp <= 90) or ((60 <= temp <= 100) and is_summer)

#Logic-1 > caught_speeding 
def caught_speeding(speed, is_birthday):
	min = 60
	max = 80
	if is_birthday:
		min = min + 5
		max = max + 5	
	if speed <= min:
		return 0
	elif max >= speed > min:
		return 1
	else: 
		return 2

#Logic-1 > sorta_sum 
def sorta_sum(a, b):
	return 20 if a + b in range (10, 20) else a + b
#alternative
def sorta_sum(a, b):
	if a + b in range (10, 20):
		return 20
	else:
		return a + b
		
#Logic-1 > alarm_clock
def alarm_clock(day, vacation):
	if day in range (1, 6) and not vacation:
		return '7:00'
	elif (day == 6 or day == 0) and vacation:
		return 'off'
	else:
		return '10:00'
#alternative
def alarm_clock(day, vacation):
	weekday = '7:00' if not vacation else '10:00'
	weekend = '10:00' if not vacation else 'off'
	return weekend if day in [0, 6] else weekday

#Logic-1 > love6 
def love6(a, b):
	return a + b == 6 or abs(a - b) == 6 or a == 6 or b == 6
#alternative
def love6(a, b):
	return 6 in [a, b, a + b, abs(a - b)]
	
#Logic-1 > in1to10 
def in1to10(n, outside_mode):
	return n >= 10 or n <= 1 if outside_mode else n in range (1, 11)

#Logic-1 > near_ten 
def near_ten(num):
	return num % 10 in [0, 1, 2, 8, 9]
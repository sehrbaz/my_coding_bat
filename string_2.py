#CodingBat Python practice problems
# String-2

#String-2 > double_char
def double_char(str):
	newstr = ''
	for i in range(len(str)):
		newstr += str[i] * 2
	return newstr

#String-2 > count_hi
def count_hi(str):
	return str.count('hi')
#alternative
def count_hi(str):
	count = 0
	for i in range(len(str)-1):
		if str[i] + str[i+1] == 'hi':
			count += 1
	return count

#String-2 > cat_dog
def cat_dog(str):
    return str.count('cat') == str.count('dog')
#alternative
def cat_dog(str):
	cat = 0
	dog = 0
	for i in range(len(str)-1):
		if str[i:i+3] == 'cat':
			cat += 1
		elif str[i:i+3] == 'dog':
			dog += 1
	return cat == dog

#String-2 > count_code
def count_code(str):
	count = 0
	for i in range(len(str)-1):
		if str[i:i+2] + str[i+3:i+4] == 'coe':
			count += 1
	return count

#String-2 > end_other
def end_other(a, b):
	dif = abs(len(a) - len(b))
	a = a.lower()
	b = b.lower()
	return a[dif:] == b or b[dif:] == a
#alternative
def end_other(a, b):
	a = a.lower(a)
	b = b.lower(b)
	return a.endswith(b) or b.endswith(a)

#String-2 > xyz_there
def xyz_there(str):
	return str.count('xyz') > str.count('.xyz')

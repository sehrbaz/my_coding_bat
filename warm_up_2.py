#CodingBat Python practice problems
#Solutions by Farid Zarbaliyev (@sehrbaz) - www.zfarid.com
# Warmup-2

#Warmup-2 > string_times 
def string_times(str, n):
	return str * n
#alternative
def string_times(str, n):
  nstr = ""
  for i in range(n):
    nstr += str
  return nstr

#Warmup-2 > front_times 
def front_times(str, n):
	return str[:3] * n

#Warmup-2 > string_bits 
def string_bits(str):
	return str [::2]

#Warmup-2 > string_splosion 
def string_splosion(str):
  str2 = ""
  for i in range(len(str)):
    str2+=str[:i]
  return str2+str

#Warmup-2 > last2 
def last2(str):
	count = 0
	for i in range (len(str)-2):
	  if str[i] + str[i+1] == str[-2:]:
		  count += 1
	return count

#Warmup-2 > array_count9 
def array_count9(nums):
	return nums.count(9)
#alternative 1
def array_count9(nums):
	count  = 0
	for n in nums
		if n == 9:
		count = count + 1
	return count
#alternative 2
def array_count9(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] == 9:
      count += 1
  return count
	
#Warmup-2 > array_front9 
def array_front9(nums):
	return 9 in (nums[:4])
#Alternative
def array_front9(nums):
	end = len(nums)
	if end > 4:
		end = 4
	for i in range(end):
		if nums[i] == 9:
			return True
	return False
	
#Warmup-2 > array123 
def array123(nums):
  for i in range(len(nums) - 2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  return False
  
#Warmup-2 > string_match 
def string_match(a, b):
  l = min(len(a), len(b))
  count = 0
  for i in range(l - 1):
    if a[i] == b[i] and a[i+1] == b[i+1]:
      count += 1
  return count
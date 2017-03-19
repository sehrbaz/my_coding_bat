#CodingBat Python practice problems
# List-2

#List-2 > count_evens
def count_evens(nums):
    count = 0
    for i in range(len(nums)):
      if nums[i] % 2 == 0:
        count += 1
    return count

#List-2 > big_diff
def big_diff(nums):
    nums.sort()
    return nums[len(nums) - 1] - nums[0]
#alternative
def big_diff(nums):
    return max(nums) - min(nums)

#List-2 > centered_average
def centered_average(nums):
    return (sum(nums) - max(nums) - min(nums)) / (len(nums) - 2)
#alternative 0
def centered_average(nums):
    nums.sort()
    nums.pop()
    nums.pop(0)
    mean = 0
    for i in nums:
     mean += i
    return mean / (len(nums))
#alternative 1
def centered_average(nums):
    mean = 0
    for i in nums:
        mean += i
    return (mean - max(nums) - min(nums)) / (len(nums) - 2)

#List-2 > sum13
def sum13(nums):
    if len(nums) == 0:
      return 0
    for i in range(len(nums)):
      if nums[i] == 13:
        nums[i] = 0
        if i+1 < len(nums):
          nums[i+1] = 0
    return sum(nums)

#List-2 > sum67
def sum67(nums):
  if len(nums) == 0:
    return 0
  while 6 in nums:
    i = nums.index(6)
    j = nums.index(7,i)
    del nums[i:j+1]
  return sum(nums)
#alternative
def sum67(nums):
    if len(nums) == 0:
        return 0
    for i in range(0, len(nums)):
        if nums[i] == 6:
            nums[i] = 0
            for j in range(i+1, len(nums)):
                  seven = nums[j]
                  nums[j] = 0
                  if seven == 7:
                    break
    return sum(nums)

#List-2 > has22
def has22(nums):
    for i in range((len(nums) - 1)):
      if nums[i] == 2 and nums[i+1] == 2:
        return True
    return False

#CodingBat Python practice problems
# List-1
# List-1 > first_last6
def first_last6(nums):
    return (nums[0] == 6) or (nums[len(nums) - 1] == 6)
#or
def first_last6(nums):
    return (nums[0] == 6 or nums[-1] == 6)

#List-1 > same_first_last
def same_first_last(nums):
    return ((len(nums) >= 1) and nums[0] == nums[-1])

#List-1 > make_pi
def make_pi():
  pi = [3, 1, 4]
  return pi

#List-1 > common_end
def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

#List-1 > sum3
def sum3(nums):
    return nums[0] + nums[1] + nums[2]
#or this one, if we do not know that array will have a lenght of 3 beforehand
def sum3(nums):
    n = len(nums)
    sum = 0
    for l in range(0, n):
        sum += nums[l]
    return sum

#List-1 > rotate_left3
def rotate_left3(nums):
    return nums + [nums.pop(0)]

#List-1 > reverse3
def reverse3(nums):
     nums.reverse()
     return nums

#List-1 > max_end3
# an easy way
def max_end3(nums):
    if nums[0] >= num[-1]:
        nums = [nums[0], nums[0], nums[0]]
        return nums
    else:
        nums = [nums[-1], nums[-1], nums[-1]]
        return nums
# imho a better approach
def max_end3(nums):
    big = max(nums[0], nums[-1])
    nums = [big, big, big]
    return nums

#List-1 > sum2
def sum2(nums):
    if len(nums) >= 2:
        return nums[0] + nums[1]
    elif len(nums) == 1:
        return nums[0]
    else:
        return 0

#List-1 > middle_way
def middle_way(a, b):
    return [a[1], b[1]]

#List-1 > make_ends
def make_ends(nums):
    return [nums[0], nums[-1]]

#List-1 > has23
def has23(nums):
    return nums.count(2) > 0 or nums.count(3) > 0

'''
USACO 2020 December Contest, Bronze
Problem 1. Do You Know Your ABCs?

10/10

http://www.usaco.org/index.php?page=viewproblem2&cpid=1059
'''

nums = list(map(int, input().strip().split(" ")))

nums.sort()

if nums[0] + nums[1] + nums[2] == nums[-1]:
    print("{} {} {}".format(str(nums[0]), str(nums[1]), str(nums[2])))
else:
    ret = False
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            for k in range(len(nums) - j - 1):
                if i != j != k and nums[i] + nums[j] in nums and nums[j] + nums[i] in nums and nums[j] + nums[k] in nums and nums[i] + nums[j] + nums[k]in nums:
                    print("{} {} {}".format(str(nums[i]), str(nums[j]), str(nums[k])))
                    ret = True
                    break
            if ret:
                break
        if ret:
            break
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i
            return len(nums)
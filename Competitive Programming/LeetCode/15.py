class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ret = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and sorted([nums[i], nums[j], nums[k]]) not in ret:
                        ret.append(sorted([nums[i], nums[j], nums[k]]))
                    if nums[i] + nums[j] + nums[k] > 0:
                        break
        return ret
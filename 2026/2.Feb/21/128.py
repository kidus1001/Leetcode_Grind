class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        best = 0
        current = 1
        nums = list(set(nums))
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                current+=1
            else:
                best = max(best, current)
                current = 1
        return max(best, current)
        """
        :type nums: List[int]
        :rtype: int
        """
        
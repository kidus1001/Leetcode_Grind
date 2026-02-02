class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        sum = 0
        minSize = float('inf')
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                minSize = min(minSize, r-l+1)
                sum -= nums[l]
                l+=1
        if float('inf') == minSize:
            return 0
        return minSize

        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
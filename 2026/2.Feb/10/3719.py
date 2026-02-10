class Solution(object):
    def longestBalanced(self, nums):
        ans = 0
        for i in range(len(nums)):
            oddCount = set()
            evenCount = set()
            for j in range(i, len(nums)):
                if nums[j]%2 == 0:
                    evenCount.add(nums[j])
                else:
                    oddCount.add(nums[j])
            
                if len(oddCount) == len(evenCount):
                    ans = max(ans, j-i+1)
        return ans

        """
        :type nums: List[int]
        :rtype: int
        """
        
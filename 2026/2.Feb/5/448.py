class Solution(object):
    def findDisappearedNumbers(self, nums):
        ans = []
        numFreq = {}
        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1
        
        for i in range(1,len(nums)+1):
            if numFreq.get(i, 0) == 0:
                ans.append(i)
        return ans

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
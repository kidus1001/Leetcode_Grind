class Solution(object):
    def maximumUniqueSubarray(self, nums):
        n = len(nums)
        l = 0
        ans = 0
        visited = set()
        sum = 0
        for r in range(n):
            while nums[r] in visited:
                num = nums[l]
                sum -= num
                visited.remove(num)
                l+=1
            visited.add(nums[r])
            sum += nums[r]
     
            ans = max (ans, sum)
        return ans
            

        """
        :type nums: List[int]
        :rtype: int
        """
        
#First approach
class Solution(object):
    def findLHS(self, nums):
        from collections import defaultdict
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        ans = float('-inf')
        for num in nums:
            length = count[num]
            upper = length + count[num+1]
            lower = length+count[ num-1]
            if count[num-1]==count[num+1]==0:
                continue
            ans = max(ans, upper)
            ans = max(ans, lower)
        return ans if ans!=float('-inf') else 0


#Second Approach
class Solution(object):
    def findLHS(self, nums):
        from collections import defaultdict
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        ans = 0
        for num in count:
            if num+1 in nums and count[num+1] + count[num] > ans:
                ans =  count[num+1] + count[num]
        return ans

#Third
class Solution(object):
    def findLHS(self, nums):
        from collections import defaultdict
        freq = Counter(nums)
        length = 0
        for num in nums:
            if num+1 in nums:
                length = max(freq[num] + freq[num+1], length)
        return length

        """
        :type nums: List[int]
        :rtype: int
        """
        
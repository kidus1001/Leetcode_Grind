class Solution(object):
    def countCompleteSubarrays(self, nums):
        n = len(nums)
        uniqueArray = set(nums)
        uniqueLen = len(uniqueArray)
        answer = 0
        for i in range(n):
            for j in range(i, n):
                subArray = set(nums[i:j+1])
                if uniqueLen == len(subArray):
                    answer+=1
        return answer
    
# Works fine, but time limit exceeds, as the time complexity is O(n2). Try using the sliding window approach.
#Two pointer approach, not optimal enough to pass all the given test cases.
class Solution(object):
    def countCompleteSubarrays(self, nums):
        l = 0
        r = 0
        n = len(nums)
        uniqueWhole = len(set(nums))
        answer = 0
        while l < n:
            if len(set(nums[l:r+1])) == uniqueWhole:
                answer+= n-r
                l += 1 
                r = l
            else:
                r+=1
            if r > n:
                l +=1
                r = l
        return answer
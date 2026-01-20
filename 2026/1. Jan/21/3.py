# class Solution(object):
#     def search(self, nums, target):
#         for i in nums:
#             if i == target:
#                 return True
#         return False
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: bool
#         """


# A bit refinement in the res and ress handling
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        res = 0
        
        for i in range(n):
            visited = set()
            for j in range(i, n):
                if s[j] not in visited:
                    visited.add(s[j])
                    res = max(res, j-i+1)
                else:
                    break
        return res
        """
        :type s: str
        :rtype: int
        """
        
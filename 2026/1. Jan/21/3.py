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
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         n = len(s)
#         res = 0
        
#         for i in range(n):
#             visited = set()
#             for j in range(i, n):
#                 if s[j] not in visited:
#                     visited.add(s[j])
#                     res = max(res, j-i+1)
#                 else:
#                     break
#         return res

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        visited = set()
        n = len(s)
        res = 0
        for r in range (n):
            while s[r] in visited:
                visited.remove(s[l])
                l+=1
            visited.add(s[r])
            res = max(res, r-l+1)
        return res
        """
        :type s: str
        :rtype: int
        """
        
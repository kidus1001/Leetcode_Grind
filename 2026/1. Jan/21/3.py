class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        res = 0
        
        for i in range(n):
            ress = 0
            visited = set()
            for j in range(i, n):
                if s[j] not in visited:
                    visited.add(s[j])
                    ress+=1
                else:
                    break
            if ress > res:
                res = ress
        return res
        """
        :type s: str
        :rtype: int
        """
        
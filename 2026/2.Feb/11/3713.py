class Solution(object):
    def longestBalanced(self, s):
        ans = 0
        for i in range(len(s)):
            current = {}
            for j in range(i, len(s)):
                current[s[j]] = current.get(s[j], 0) + 1

                size = current[s[j]]
                check = True
                for k,v in current.items():
                    if v != size:
                        check = False
                if check:
                    ans = max(ans, j-i+1)
        return ans

        """
        :type s: str
        :rtype: int
        """
        
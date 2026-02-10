class Solution(object):
    def minWindow(self, s, t):
        ans = ""
        firstFill = False
        if len (t) > len(s):
            return ""
        target = {}
        for ch in t:
            target[ch] = target.get(ch, 0) + 1
        
        curWindow = {}
        l = 0
        checker = 0
        for r in range(len(s)):
            # if s[r] in target:
            curWindow[s[r]] = curWindow.get(s[r], 0) + 1
            if s[r] in target and curWindow[s[r]] == target[s[r]]:
                checker += 1
                
            # checker == len(target) and l <= r
            while checker == len(target) and l<=r:
                potentialAns = s[l:r+1]
                if not firstFill:
                    ans = s
                    firstFill = True
                if len(potentialAns) < len(ans):
                    ans = potentialAns

                if s[l] in target and curWindow[s[l]] == target[s[l]]:
                    checker -= 1
                curWindow[s[l]] = curWindow.get(s[l], 0) - 1
                
                l+=1
        return ans



        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
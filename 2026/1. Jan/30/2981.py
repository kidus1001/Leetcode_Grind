from collections import defaultdict
class Solution(object):
    def maximumLength(self, s):
        stringDict = defaultdict(int)
        n = len(s)
        for i in range(n):
            for j in range(i, n+1):
                subS = s[i:j]
                stringDict[subS] += 1
        stringDict = {k: v for k, v in stringDict.items() if k.strip()}

        ans = 0
        for k, v in stringDict.items():
            if v > 2:
                boolC = True
                s = len(k)
                first = k[0]
                for i in range(1, s):
                    if k[i] != first:
                        boolC = False
                        break
                if s > ans and boolC:
                    print(k)
                    ans = s
        
        if ans == 0:
            return -1
        return ans
            

        """
        :type s: str
        :rtype: int
        """
        
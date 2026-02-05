class Solution(object):
    def checkInclusion(self, s1, s2):
        from collections import Counter

        if len(s1) > len(s2):
            return False

        targetFreq = Counter(s1)
        l = 0
        match = 0

        curWindow = {}
        for i in range(len(s1)):
            curWindow[s2[i]] = curWindow.get(s2[i], 0) + 1
            if curWindow[s2[i]] == targetFreq[s2[i]]:
                match +=1
        for r in range(len(s1), len(s2)):
            if match == len(targetFreq):
                return True
            curWindow[s2[r]] = curWindow.get(s2[r], 0) + 1
            if curWindow[s2[r]] == targetFreq[s2[r]]:
                match +=1
            if curWindow[s2[l]] == targetFreq[s2[l]]:
                match -= 1
            curWindow[s2[l]] = curWindow.get(s2[l], 0) - 1
            l+=1
        if match == len(targetFreq):
                return True
        return False

        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
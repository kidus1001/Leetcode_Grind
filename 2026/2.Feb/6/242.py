class Solution(object):
    def isAnagram(self, s, t):
        mapStr1 = {}
        mapStr2 = {}
        if len(s) != len(t):
            return False
        
        i = 0
        while i < len(s):
            mapStr1[s[i]] = mapStr1.get(s[i], 0) + 1
            mapStr2[t[i]] = mapStr2.get(t[i], 0) + 1
            i += 1

        for ch in mapStr1:
            if mapStr1[ch] != mapStr2.get(ch, 0):
                return False
        return True

        """
        :type s: str
        :type t: str
        :rtype: bool
        """



#Lazy Code
class Solution(object):
    def isAnagram(self, s, t):
        sT = sorted(t)
        if sorted(s) == sT:
            return True
        else:
            return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
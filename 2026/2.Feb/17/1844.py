class Solution(object):
    def replaceDigits(self, s):
        if len(s) == 1:
            return s
        s = list(s)
        i = 0
        while i < len(s)-1:
            s[i+1] = chr((((ord(s[i]) + int(s[i+1])) - 97) % 26) + 97)
            i+=2
        return "".join(s)
        """
        :type s: str
        :rtype: str
        """
        
class Solution(object):
    def shiftingLetters(self, s, shifts):
        total = 0
        for i in range(len(shifts)-1, -1, -1):
            total += shifts[i]
            shifts[i] = total % 26
        
        s = list(s)
        for i in range(len(s)):
            s[i] = chr (((ord(s[i]) - 97 + shifts[i]) % 26) + 97)
        return "".join(s)
        """ 
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        
class Solution(object):
    def findLUSlength(self, a, b):
        if len(a) > len(b):
            return len(a)
        elif (len(a) < len(b)):
            return len(b)


        ans = 0
        for i in range (0, len(a)):
            if a[i] != b[i]:
                ans += 1
            
        if ans == 0:
            return -1
        return len(a)

        """
        :type a: str
        :type b: str
        :rtype: int
        """
        
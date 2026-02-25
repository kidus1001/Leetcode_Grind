class Solution(object):
    def canWinNim(self, n):
        if 1 <= n%4 <= 3:
            return True
        else:
            return False 
        """
        :type n: int
        :rtype: bool
        """
        
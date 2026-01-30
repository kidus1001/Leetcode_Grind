import math
class Solution(object):
    def isPerfectSquare(self, num):
        num = math.sqrt(num)
        floorNum = math.floor(num)
        if num == floorNum:
            return True
        else:
            return False
        
# Redo it using binary search, or something other than this 'sqrt' thing

        """
        :type num: int
        :rtype: bool
        """
        
class Solution(object):
    def sumOfThree(self, num):
        if num%3 != 0:
            return []
        x = num//3
        ans = []
        ans.append(x-1)
        ans.append(x)
        ans.append(x+1)
        return ans
        """
        :type num: int
        :rtype: List[int]
        """
        
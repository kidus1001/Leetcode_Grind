class Solution(object):
    def magicalString(self, n):
        magicalStr = [1,2,2]
        left = 2
        nextNum = 1
        for i in range(99997):
            if magicalStr[left] == 2:
                magicalStr.append(nextNum)
                magicalStr.append(nextNum)
            else:
                magicalStr.append(nextNum)
            if nextNum == 1:
                nextNum = 2
            else:
                nextNum = 1
            left += 1
        ans = 0
        for i in range(n):
            if magicalStr[i] == 1:
                ans+=1
        return ans
            
        """
        :type n: int
        :rtype: int
        """
        
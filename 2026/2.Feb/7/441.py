class Solution:
    def arrangeCoins(self, n: int) -> int:
        totalSum = 0
        init = 1
        while totalSum <= n:
            totalSum += init
            init+=1
        return init-2
        

class Solution(object):
    def totalFruit(self, fruits):
        from collections import defaultdict

        count = defaultdict(int)
        l = 0
        maxAns = float('-inf')

        for r in range(len(fruits)):
            count[fruits[r]] += 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l+=1
            maxAns = max(maxAns, r-l+1)

        return maxAns
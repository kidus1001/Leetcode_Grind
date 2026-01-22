class Solution(object):
    def minimumCardPickup(self, cards):
        n = len(cards)
        l = 0
        visited = set()
        ans = -1
        for r in range(n):
            while (cards[r] in visited):
                visited.remove(cards[l])
                if cards[r] == cards[l]:
                    if ans == -1:
                        ans = r-l+1
                    else:
                        ans = min(ans, r-l+1)
                l+=1
            visited.add(cards[r])
        return ans
            

        """
        :type cards: List[int]
        :rtype: int
        """
        
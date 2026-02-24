class Solution(object):
    def uniqueOccurrences(self, arr):
        from collections import Counter
        count = Counter(arr)
        
        occ = []
        for i in count:
            occ.append(count[i])
        
        occ.sort()
        for i in range(len(occ)-1):
            if occ[i] >= occ[i+1]:
                return False
        return True
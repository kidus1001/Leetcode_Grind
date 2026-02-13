class Solution(object):
    def groupAnagrams(self, strs):
        hashTablesList = []
        for st in strs:
            hashtable = {}
            for ch in st:
                hashtable[ch] = hashtable.get(ch, 0) + 1
            hashTablesList.append(hashtable)
        ans = []
        visited = []
        for i in range(len(strs)):
            if strs[i] in visited:
                continue
            ansA = []
            for j in range(i, len(strs)):
                if hashTablesList[i] == hashTablesList[j]:
                    ansA.append(strs[j])
                    visited.append(strs[j])
            ans.append(ansA)
        return ans
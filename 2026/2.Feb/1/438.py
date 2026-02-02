#Need to redo it

class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        target = {}
        for ch in p:
            target[ch] = target.get(ch, 0) + 1

        missing = len(p)
        ans = []
        l = 0

        for r in range(len(s)):
            # character enters the window
            if s[r] in target:
                if target[s[r]] > 0:
                    missing -= 1
                target[s[r]] -= 1

            # shrink window if size exceeds p
            if r - l + 1 > len(p):
                if s[l] in target:
                    if target[s[l]] >= 0:
                        missing += 1
                    target[s[l]] += 1
                l += 1

            # check invariant
            if missing == 0:
                ans.append(l)#
        return ans

# class Solution(object):
#     def findAnagrams(self, s, p):
#         l = 1
#         k = len(p)
#         ans = []
#         target = {}
#         missing = k
#         for ch in p:
#             target[ch] = target.get(ch,0) + 1

        
#         for i in range(k):
#             if s[i] in target:
#                 target[s[i]] = target[s[i]] - 1
#                 if target[s[i]] > 0:
#                     missing-=1
#             else:
#                 target[s[i]] = 0

#         if missing == 0:
#             ans.append(0)

#         for r in range(k, len(s)-k+1):
#             if s[l-1] in target:
#                 target[s[l-1]] = target[s[l-1]] + 1
#                 if target[s[i]] > 0:
#                     missing+=1
#             else:
#                 target[s[l-1]] = 0

#             if s[r] in target:
#                 target[s[r]] = target[s[r]] - 1
#                 missing -= 1
#             else:
#                 target[s[r]] = 0

#             if missing == 0:
#                 ans.append(l)
#             l+=1
#         return ans


#         #     win = s[l:l+k]
#         #     if sorted(win) == sorted(p):
#         #         ans.append(l)
#         #     l+=1
#         # return ans


#         """
#         :type s: str
#         :type p: str
#         :rtype: List[int]
#         """
        
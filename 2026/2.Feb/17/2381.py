# Efficient solution using prefix sum
class Solution(object):
    def shiftingLetters(self, s, shifts):
        my_dict = {
            "a": 0, "b": 1, "c": 2, "d": 3, "e": 4,
            "f": 5, "g": 6, "h": 7, "i": 8, "j": 9,
            "k": 10, "l": 11, "m": 12, "n": 13, "o": 14,
            "p": 15, "q": 16, "r": 17, "s": 18, "t": 19,
            "u": 20, "v": 21, "w": 22, "x": 23, "y": 24,
            "z": 25
        }
        rev_dict = {v: k for k, v in my_dict.items()}
        prefix = [0] * (len(s) + 1)
        for i in range(len(shifts)):
            l = shifts[i][0]
            r = shifts[i][1]
            command = shifts[i][2]
            if command == 1:
                prefix[r+1] += 1
                prefix[l] -= 1
            else:
                prefix[r+1] -= 1
                prefix[l] += 1
        
        ansRev = ""
        tracker = 0
        for i in range(len(s), 0, -1):
            tracker += prefix[i]
            trackerCopy = tracker + my_dict[s[i-1]]
            while trackerCopy < 0:
                trackerCopy += 26
            trackerCopy %= 26

            ansRev += rev_dict[trackerCopy]

        return ansRev[::-1]




# Not efficient enough code. Try again using prefix sum.
# class Solution(object):
#     def shiftingLetters(self, s, shifts):
#         count = [0] * len(s)
#         for i in range(len(shifts)):
#             if shifts[i][2] == 0:
#                 for j in range(shifts[i][0], shifts[i][1]+1):
#                     count[j] -= 1
#             else:
#                 for j in range(shifts[i][0], shifts[i][1]+1):
#                     count[j] += 1
        
#         my_dict = {
#             "a": 0, "b": 1, "c": 2, "d": 3, "e": 4,
#             "f": 5, "g": 6, "h": 7, "i": 8, "j": 9,
#             "k": 10, "l": 11, "m": 12, "n": 13, "o": 14,
#             "p": 15, "q": 16, "r": 17, "s": 18, "t": 19,
#             "u": 20, "v": 21, "w": 22, "x": 23, "y": 24,
#             "z": 25
#         }

#         rev_dict = {v: k for k, v in my_dict.items()}
#         i = 0
#         ans = ""
#         for ch in s:
#             posS = my_dict[ch]
#             posS += count[i]
#             a = posS
#             i+=1
#             if a < 0:
#                 while a > 0:
#                     a = 26 + a
#             a = a % 26

#             ans += rev_dict[a]

#         return ans
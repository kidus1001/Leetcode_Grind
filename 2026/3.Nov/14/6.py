class Solution(object):
    def freqAlphabets(self, s):
        hashmap = {}
        start = 'a'
        for i in range (1, 10):
            hashmap[str(i)] = start
            start = chr(ord(start) + 1)
        
        init = 10
        start = 'j'
        for i in range (10, 27):
            key = str (str(i) + "#")
            hashmap[key] = start
            start = chr(ord(start) + 1)

        ans = ""
        
        i = len(s)-1
        while i >= 0:
            if s[i] != "#":
                ans += hashmap[s[i]]
                i-=1
            
            else:
                cur = s[i]
                cur += s[i-1]
                cur += s[i-2]

                rev = cur[::-1]
                i -= 3
                ans += hashmap [rev]

        
        return ans[::-1]
        
        """
        :type s: str
        :rtype: str
        """
        
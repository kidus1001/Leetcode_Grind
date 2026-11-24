class Solution(object):
    def detectCapitalUse(self, word):
        countUpper = 0
        for i in range(len(word)):
            if word[i].isupper():
                countUpper += 1
        
        if countUpper == 0 or countUpper == len(word) or (word[0].isupper() and countUpper == 1):
            return True
        
        return False

        """
        :type word: str
        :rtype: bool
        """
        
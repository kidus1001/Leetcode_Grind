class Solution(object):
    def detectCapitalUse(self, word):
        if word.isupper():
            return True
        if word.islower():
            return True
        
        if word[0].isupper():
            for i in range(1, len(word)):
                if word[i].islower():
                    continue
                return False
            return True
        return False
        """
        :type word: str
        :rtype: bool
        """
        
class Solution(object):
    def detectCapitalUse(self, word):
        smallMin = 97
        smallMax = 122
        capMin = 65
        capMax = 90

        rule1 = True
        

        for i in range (len(word)):
            if not (ord(word[i]) >= capMin and ord(word[i]) <= capMax):
                rule1 = False
                break  

        if rule1:
            return True

        rule2 = True
        
        for i in range (len(word)):
            if not (ord(word[i]) >= smallMin and ord(word[i]) <= smallMax):
                rule2 = False
                break

        if rule2:
            return True

        rule3 = True
        i = 0

        if not (ord(word[i]) >= capMin and ord(word[i]) <= capMax):
            rule3 = False
        
        if not rule3:
            return False
        
        i+=1

        while i < len(word):
            if not (ord(word[i]) >= smallMin and ord(word[i]) <= smallMax):
                rule3 = False
                break
            i+=1
            

        if rule3:
            return True

        return False
        """
        :type word: str
        :rtype: bool
        """
        
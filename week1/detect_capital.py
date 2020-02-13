class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)==1:
            return True
        
        if 97<=ord(word[0])<=122: # first char lower
            for i in range(1, len(word)):
                if ord(word[i])<97 or ord(word[i])>122:
                    return False
        else:
            if 97<=ord(word[1])<=122:
                for i in range(2, len(word)):
                    if ord(word[i])<97 or ord(word[i])>122:
                        return False 
            else:
                for i in range(2, len(word)):
                    if ord(word[i])<65 or ord(word[i])>90:
                        return False 
        
        return True
        

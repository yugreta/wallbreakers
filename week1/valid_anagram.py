class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        
        s_chars = {}
        for c in s:
            if s_chars.get(c):
                s_chars[c]+=1
            else:
                s_chars[c]=1
        
        for c in t:
            if not s_chars.get(c):
                return False
            s_chars[c]-=1
            if s_chars[c]==0:
                s_chars.pop(c)
                
        return not len(s_chars)

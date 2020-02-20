import collections

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = collections.Counter(s)
        for i in range(len(s)):
            if chars[s[i]]==1:
                return i
        return -1

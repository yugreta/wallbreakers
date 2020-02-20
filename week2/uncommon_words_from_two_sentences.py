from collections import defaultdict

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        words = defaultdict(int)
        for word in A.split():
            words[word] += 1
        for word in B.split():
            words[word] += 1
        words = list(k for k in words if  words[k]==1)
        
        return words

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        sorted = []
        odds = []
        for i in A:
            if i%2==0:
                sorted.append(i)
            else:
                odds.append(i)
        sorted.extend(odds)
        return sorted

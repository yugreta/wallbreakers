class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        num = x^y
        distance = 0
        while num:
            if num&1:
                distance += 1
            num >>= 1
        return distance

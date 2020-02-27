class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n==1:
            return x
        split = self.myPow(x, int(abs(n)/2))
        if n%2==0:
            split = split*split
        else:
            split = split*split*x
        if n>0:
            return split
        else:
            return 1/split

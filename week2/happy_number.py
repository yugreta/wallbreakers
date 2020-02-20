class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        not_happy = {n}
        while True:
            sum = 0
            while n>=1:
                sum += (n%10)**2
                n = int(n/10)
            if sum == 1:
                return True
            elif sum in not_happy:
                return False
            else:
                not_happy.add(sum)
                n = sum

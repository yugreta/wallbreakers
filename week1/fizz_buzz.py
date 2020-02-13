class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        altered_n = []
        for i in range(1, n+1):
            if i%3 == 0:
                if i%5 ==0:
                    altered_n.append("FizzBuzz")
                else:
                    altered_n.append("Fizz")
            elif i%5 == 0:
                altered_n.append("Buzz")
            else:
                altered_n.append(str(i))
        return altered_n
        

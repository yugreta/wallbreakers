class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        complement = ''
        for bit in bin(num)[2:]:
            complement += ('0' if bit=='1' else '1')
        return int(complement, 2)
        

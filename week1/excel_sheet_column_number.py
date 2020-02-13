class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        column_num = 0
        
        power = len(s)-1
        for char in s:
            column_num += (ord(char)-64)*(26**power)
            power -= 1
        
        return column_num

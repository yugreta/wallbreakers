class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        try:
            i = -1
            while (digits[i] == 9):
                digits[i] = 0
                i -= 1
            digits[i]+=1
            return digits
        except IndexError:
            larger_integer = [1]
            larger_integer.extend(digits)
            return larger_integer

class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        gap = 0
        running_gap = 0
        for bit in bin(N)[3:]:
            running_gap += 1
            if bit=='1':
                if running_gap > gap:
                    gap = running_gap
                running_gap = 0
        return gap

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = {j for j in J}
        our_jewels = 0
        for s in S:
            if s in jewels:
                our_jewels += 1
        return our_jewels

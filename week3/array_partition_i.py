class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sorts, keep even indexed, sum
        return sum(sorted(nums)[::2])

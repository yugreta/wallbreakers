class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min = 0
        max = len(nums)-1
        while min<=max:
            mid = int((max+min)/2)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                min = mid + 1
            else:
                max = mid - 1
        return -1

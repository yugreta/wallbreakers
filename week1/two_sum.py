class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        matching_pairs = {}
        
        for i in range(len(nums)):
            if matching_pairs.get(nums[i]) != None: # 0 is valid index
                return [matching_pairs[nums[i]], i]
            else:
                matching_pairs[target-nums[i]] = i
                
        return []

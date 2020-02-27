class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        front = 1
        end = len(A)-2
        while True:
            i = int((front+end)/2)
            if A[i] > A[i-1]:
                if A[i] > A[i+1]:
                    return i
                else:
                    front = i+1
            else:
                end = i-1
        return -1

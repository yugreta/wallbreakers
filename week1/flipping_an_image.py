class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        new_image = []
        for row in range(len(A)):
            reversed_col = len(A[row])-1
            new_col = []
            for col in range(len(A[row])):
                new_col.append(0 if A[row][reversed_col] else 1)
                reversed_col -= 1
            new_image.append(new_col)
        return new_image
        

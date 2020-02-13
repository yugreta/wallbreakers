class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        matrix_transpose = []
        for row in range(len(A[0])):
            new_col = []
            for col in range(len(A)):
                new_col.append(A[col][row])
            matrix_transpose.append(new_col)
        return matrix_transpose
        

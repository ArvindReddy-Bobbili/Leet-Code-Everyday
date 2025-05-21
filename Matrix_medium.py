class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zerorows = set()
        zerocols = set()
        for i in range(m):#2
            for j in range(n):#2
                if(matrix[i][j]==0):
                    zerorows.add(i)
                    zerocols.add(j)
        for i in zerorows:
            for j in range(n):
                matrix[i][j]=0
        for i in range(m):
            for j in zerocols:
                matrix[i][j] =0

                    
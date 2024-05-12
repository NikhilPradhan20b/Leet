class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        new_matrix = [[0 for j in range(len(grid)-2)] for i in range(len(grid)-2)]
        test1 = 0
        test = 0
        count = len(new_matrix)*len(new_matrix)
        k = l = 0 
        while count>0:
            Max = 0 
            for i in range(test,test+3):
                for j in range(test1,test1+3):
                    # print(grid[i][j])
                    Max = max(Max,grid[i][j])
            
            new_matrix[k][l] = Max
            l+=1
            if l==len(new_matrix):
                l=0
                k+=1
            test1+=1
            if test1+2==len(grid):
                test1=0
                test+=1
            count-=1
        return new_matrix

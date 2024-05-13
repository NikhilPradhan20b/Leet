class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        def flip(value):
            if value==0:
                return 1
            else:
                return 0
        for i in range(len(grid)):
                if grid[i][0]==0:
                    for j in range(len(grid[i])):
                        grid[i][j]=flip(grid[i][j])
        for i in range(1,len(grid[0])):
            count_0 = 0
            count_1 = 0
            for j in range(len(grid)):
                if grid[j][i]==0:
                    count_0+=1
                else:
                    count_1+=1
            if count_0>count_1:
                for j in range(len(grid)):
                    grid[j][i]=flip(grid[j][i])
        Sum = 0
        for i in range(len(grid)):
            temp = ''
            for j in range(len(grid[0])):
                temp+=str(grid[i][j])
            Sum+=int(temp, 2)
        return Sum
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_set = defaultdict(int)
        column_set = defaultdict(int)
        for i in range(len(grid)):
            temp1 = []
            temp2 = []
            for j in range(len(grid)):
                temp1.append(grid[i][j])
                temp2.append(grid[j][i])
            temp1 = tuple(temp1)
            temp2 = tuple(temp2)
            row_set[temp1]+=1
            column_set[temp2]+=1
        count=0
        for each in row_set:
            if each in column_set:
                count+=row_set[each]*column_set[each]
                
        return(count)
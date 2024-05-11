class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        check = set()
        for i in range(1,len(matrix)+1):
            check.add(i)
        print(check)
        for i in range(len(matrix)):
            row_check = set()
            column_check = set()
            for j in range(len(matrix)):
                row_check.add(matrix[j][i])
                column_check.add(matrix[i][j])
            if len(row_check)!=len(check) or len(column_check)!=len(check):
                return False
            else:
                for each in check:
                    if each not in row_check or each not in column_check:
                        print(each)
                        return False
        return True

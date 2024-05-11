class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        check = set()
        for i in range(1,len(matrix)+1):
            check.add(i)
        for i in range(len(matrix)):
            row_check = set()
            column_check = set()
            for j in range(len(matrix)):
                row_check.add(matrix[j][i])
                column_check.add(matrix[i][j])
            # print(row_check,column_check,check,row_check==check)
            # if len(row_check)!=len(check) or len(column_check)!=len(check):
            #     return False
            # else:
            #     for each in check:
            #         if each not in row_check or each not in column_check:
            #             return False
            if row_check!=check or column_check!=check:
                return False
        return True

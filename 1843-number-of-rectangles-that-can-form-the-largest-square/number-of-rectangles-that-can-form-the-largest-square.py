class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        arr = []
        Max = float('-inf')
        for each in rectangles:
            check= min(each[0],each[1])
            arr.append(check)
            Max = max(Max,check)
        count = 0
        for each in arr:
            if each==Max:
                count+=1
        return count
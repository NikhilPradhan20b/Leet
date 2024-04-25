class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        Max = 0
        for each in accounts:
            Max = max(Max,sum(each))
        return Max
        
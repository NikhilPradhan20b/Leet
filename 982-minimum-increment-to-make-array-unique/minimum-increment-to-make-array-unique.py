class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        new_set = set()
        ans = 0
        Max = 0
        for num in nums:
            if num not in new_set:
                new_set.add(num)
                Max = num
            else:
                ans+=Max+1-num
                new_set.add(Max+1)
                Max = Max+1
        return ans
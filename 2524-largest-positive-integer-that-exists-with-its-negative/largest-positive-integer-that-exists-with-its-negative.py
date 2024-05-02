class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums)-1
        while i<j:
            if nums[i] * -1 == nums[j]:
                return nums[j]
            else:
                if nums[j] > nums[i] * -1:
                    j-=1
                else:
                    i+=1
        return -1

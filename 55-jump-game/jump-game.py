class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums)-2
        threshold=1
        while i>0:
            if nums[i]<threshold:
                threshold +=1
            else:
                threshold=1
            i-=1

        if len(nums)>1 and threshold>nums[0]:
            return False
        else:
            return True      
        
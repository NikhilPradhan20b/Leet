class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Sum = sum(nums)-nums[0]
        presum = 0
        for i in range(len(nums)-1):
            if presum==Sum:
                return i
            presum+=nums[i]
            Sum -= nums[i+1]

        if sum(nums) - nums[-1] == 0:
            return len(nums)-1
            
        return -1
        
            
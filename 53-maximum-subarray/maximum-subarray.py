class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # l=0
        # r=len(nums)-1
        # ans =temp= sum(nums)

        # while l<r:
        #     if nums[l]<nums[r]:
        #         temp-=nums[l]
        #         l+=1
        #     else:
        #         temp-=nums[r]
        #         r-=1
        #     ans = max(ans,temp)
            
        # return(ans)
        maxSum = float('-inf')
        currentSum = 0
        
        for num in nums:
            currentSum += num
            
            if currentSum > maxSum:
                maxSum = currentSum
            
            if currentSum < 0:
                currentSum = 0
        
        return maxSum
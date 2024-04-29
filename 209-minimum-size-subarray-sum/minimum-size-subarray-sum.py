class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        win_sum=0
        i=0
        j=0
        ans= 9999999
        while i<len(nums):
            if win_sum>=target:
                ans = min(ans,j-i)
                win_sum-=nums[i]
                i+=1
            else:
                if j<len(nums):

                    win_sum +=nums[j]
                    j+=1
                else:
                    i+=1  
        if ans==9999999:
            return 0
        return ans

            
        
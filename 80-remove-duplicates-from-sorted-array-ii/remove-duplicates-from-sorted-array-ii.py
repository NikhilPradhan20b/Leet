class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        count = 0
        while i<len(nums):
            if count == 0:
                current = nums[i]
                count+=1
                i+=1
            elif count>1 and nums[i]==current:
                nums.pop(i)
            elif nums[i]!=current:
                current = nums[i]
                count=1
                i+=1
            else:
                count+=1
                i+=1
        return len(nums)
            
                
        
            
            
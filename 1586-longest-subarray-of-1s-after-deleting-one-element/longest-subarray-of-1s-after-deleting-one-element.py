class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        hasm = {}
        for i in range(len(nums)):
            if nums[i]==0:
                hasm[i]=nums[i]
        print(hasm)
        ans = 0
        if hasm:
            if len(hasm)==1:
                return(len(nums)-1)
            test = list(hasm.keys())
            test.append(len(nums))
            if len(test)==2:
                return(max(test[1]-test[0]-1,test[1]-1,len(nums)-test[1]-1))
            print(test)
            for i in range(len(test)):
                if i==0:
                    ans = max(ans,test[i+1]-1)
                elif i==len(test)-1:
                    ans = max(ans,test[i-1]-test[i-2]-1)
                else:
                    ans = max(ans,test[i+1]-(test[i-1]+1)-1)
            return(ans)
        else:
            return(len(nums)-1)
    

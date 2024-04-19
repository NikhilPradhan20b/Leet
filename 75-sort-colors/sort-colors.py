class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]*3
        for num in nums:
            if num==0:
                count[0]+=1
            elif num==1:
                count[1]+=1
            else:
                count[2]+=1
        j=0
        i=0
        while j<3:
            if count[j]>0:
                if j==0:
                    nums[i]=0
                elif j==1:
                    nums[i]=1
                else:
                    nums[i]=2
                i+=1
                count[j]-=1
            else:
                j+=1
            

                
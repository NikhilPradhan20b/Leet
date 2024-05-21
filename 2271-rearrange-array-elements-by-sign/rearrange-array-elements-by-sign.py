class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        ans = []
        if nums[0]>0:
            first = True
        else:
            first = False
        for each in nums:
            if each>0:
                pos.append(each)
            else:
                neg.append(each)
        if first:
            for i in range(len(pos)):
                ans.append(pos[i])
                ans.append(neg[i])
        else:
            for i in range(len(pos)):
                ans.append(pos[i])
                ans.append(neg[i])
        return ans

            
            
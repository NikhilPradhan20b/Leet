class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hasm={}
        for i in range(len(nums)):
            if nums[i] not in hasm.keys():
                hasm[nums[i]] = i
            else:
                if abs(hasm[nums[i]]-i)<=k:
                    return True
                else:
                    hasm[nums[i]]=i
        return False
        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        m=0
        while l<=r:
            m=(l+r)//2
            midnum=nums[m]
            if midnum==target:
                return m
            if midnum<target:
                l=m+1
            else:
                r=m-1
        return -1
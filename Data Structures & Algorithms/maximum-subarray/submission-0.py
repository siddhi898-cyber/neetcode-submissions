class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs,ms=0,nums[0]
        for i in range(len(nums)):
            cs=cs+nums[i]
            ms=max(cs,ms)
            if cs<0:
                cs=0
        return ms

        
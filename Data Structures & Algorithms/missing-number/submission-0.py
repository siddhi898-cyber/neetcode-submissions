class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=len(nums)#we start with n
        
        for i in range(len(nums)):
            res=res+(i-nums[i])             #add the expected number i and subtract the actual number nums[i]
        return res   #present numbers cancel out and the remaining number is returned
                                                
        
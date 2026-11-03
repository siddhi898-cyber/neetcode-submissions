class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range (len(nums)):
            if nums.count(i)>1:
                return True
            else :
                return False
        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=None
        count=0
        for i in nums:
            if count==0:
                c=i
            elif count==c:
                count=count+1
            else:
                count =count-1
        return c
        

        
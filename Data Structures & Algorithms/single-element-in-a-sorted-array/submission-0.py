class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        l,r=0,n-1
        if n==1:
            return nums[0]
        while l<r:
            mid=(l+r)//2
            
            if mid%2==0:
                if nums[mid]==nums[mid-1]:
                    r=mid-2
                else:
                    l=mid+2
            else:
                if nums[mid]==nums[mid-1]:
                    l=mid+1
                else:
                    r=mid-1
        return nums[l]

        
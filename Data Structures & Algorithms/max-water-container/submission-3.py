class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        l,r=0,n-1
        maxa=0
        while l<r:
            w=r-l
            ht=min(heights[l], heights[r])
            a=w*ht
            if heights[l]<heights[r]:
                l=l+1
            else:
                r=r-1
            maxa=max(maxa,a)
        return maxa

                    
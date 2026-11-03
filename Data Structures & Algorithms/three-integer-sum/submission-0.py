class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()  # Stores unique triplets

        n = len(nums)

        for i in range(n):                 # First number
            for j in range(i + 1, n):      # Second number, after i
                for k in range(j + 1, n):  # Third number, after j
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(triplet)  # Set removes duplicates automatically

        return [list(triplet) for triplet in result]
        
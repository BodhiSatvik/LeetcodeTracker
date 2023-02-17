class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            # Base case
            if i == len(nums):
                res.append(subset[::])
                return
            
            # Decision to include i in our algo
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            # Increment i in case of duplicate value
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            backtrack(i+1, subset)
        
        backtrack(0, [])
        return res
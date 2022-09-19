class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        
        while l <= r:
            # In the sorted portion
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            
            mid = (l + r) // 2
            res = min(res, nums[mid])
            
            # Left portion
            if nums[l] <= nums[mid]:
                l = mid + 1
            else: # Right portion
                r = mid - 1
        
        return res
            
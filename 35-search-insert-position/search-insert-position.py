class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            print(m)
            if nums[m] == target: return m
            # search right half
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return m + 1 if nums[m] < target else m 
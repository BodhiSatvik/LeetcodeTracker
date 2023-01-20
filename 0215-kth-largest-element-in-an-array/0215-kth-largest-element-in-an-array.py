class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k       # kth largest is also (n-k)th smallest
        
        def recFun(l, r):
            p, pivot = l, nums[r]
            
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            
            if p < k: return recFun(p+1, r)
            if p > k: return recFun(l, p-1)
            else: return nums[p]
        
        return recFun(0, len(nums) - 1)
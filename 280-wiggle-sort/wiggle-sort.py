class Solution:
    
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        nums.sort()
        for i in range(1, len(nums) - 1, 2):
            swap(nums, i, i + 1)
        

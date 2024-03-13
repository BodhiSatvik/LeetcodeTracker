class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {} # [num: idx]
        for i, num in enumerate(nums):
            if (target - num) in num_idx:
                # return the index of 
                return (i, num_idx[target-num])
            num_idx[num] = i


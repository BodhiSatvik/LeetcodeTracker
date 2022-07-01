class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)):
        #     var = nums[i]
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        #         else:
        #             j+=1
        #     i+=1
        
        hash_map = {}
        for i, n in enumerate(nums):
            diff = target-n
            if diff in hash_map:
                return [hash_map[diff], i]
            else:
                hash_map[n] = i
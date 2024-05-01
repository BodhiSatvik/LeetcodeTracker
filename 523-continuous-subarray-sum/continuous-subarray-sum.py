class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = { 0: -1 }
        curSum = 0
        for i, n in enumerate(nums):
            curSum += n
            r = curSum % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] >= 2:
                return True
        return False

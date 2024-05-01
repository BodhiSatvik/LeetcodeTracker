class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = { 0: -1 }
        curSum = 0
        for i, n in enumerate(nums):
            curSum += n
            if (curSum % k) not in remainder:
                remainder[curSum % k] = i
            elif curSum%k in remainder and i - remainder[curSum % k] >= 2:
                return True
        return False

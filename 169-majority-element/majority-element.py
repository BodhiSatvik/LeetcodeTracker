class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = collections.Counter(nums)
        return max(majority, key=majority.get)
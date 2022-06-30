class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hesh = set()
        for i in nums:
            if i in hesh:
                return True
            else:
                hesh.add(i)
        return False
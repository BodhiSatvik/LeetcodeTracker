class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hesh = set()
        for i in nums:
            if i not in hesh:
                hesh.add(i)
            else:
                return True
        return False
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        wordset = set()
        res = 0
        while r < len(s):
            while s[r] in wordset:
                wordset.remove(s[l])
                l += 1
            wordset.add(s[r])
            r += 1
            res = max(res, len(wordset))
        return res

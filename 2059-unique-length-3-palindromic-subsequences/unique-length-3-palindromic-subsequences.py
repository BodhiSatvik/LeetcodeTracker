class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letter = set(s)
        res = 0 

        for c in letter:
            f, l = s.index(c), s.rindex(c)
            between = set()

            for i in range(f+1, l):
                between.add(s[i])
            res += len(between)
        return res



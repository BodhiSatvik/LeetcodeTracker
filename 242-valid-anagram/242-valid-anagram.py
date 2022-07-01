class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if collections.Counter(s) != collections.Counter(t):
        #     return False
        hesh1 = {}
        hesh2 = {}
        for i in s:
            if i in hesh1:
                hesh1[i] += 1
            else:
                hesh1[i] = 1
        
        for i in t:
            if i in hesh2:
                hesh2[i] += 1
            else:
                hesh2[i] = 1
        
        return hesh1 == hesh2
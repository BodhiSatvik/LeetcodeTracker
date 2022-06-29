class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        hesh = {}
        for i in s:
            if i in hesh:
                hesh[i] += 1
            else:
                hesh[i] = 1
        
    
        for value in hesh.values():
            ans += value //2*2
            if (ans % 2 == 0) and (value%2==1):
                ans += 1
        return ans
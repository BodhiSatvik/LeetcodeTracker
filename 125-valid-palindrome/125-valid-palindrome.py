class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for i in s:
            if i.isalnum():
                new_s += i.lower()
        
        if len(new_s) <= 1:
            return True
        back = len(new_s) - 1
        
        for front in range(len(new_s) // 2):
            if new_s[front] == new_s[back]:
                back -= 1
            else:
                return False
        return True
        
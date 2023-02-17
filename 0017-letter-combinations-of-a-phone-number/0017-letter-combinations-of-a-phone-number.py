class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        s = ''

        table = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }

        def dfs(i, s):
            if i == len(digits):
                res.append(s[:])
                return
            for letter in table[int(digits[i])]:
                s += letter
                dfs(i+1, s)
                s = s[:-1]
        
        if digits:
            dfs(0, s)
        return res
            




class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, sub, total):
            if total == target:
                res.append(sub.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            # two decisions

            # go with current i
            sub.append(candidates[i])
            dfs(i, sub, total + candidates[i])
            
            # don't
            sub.pop()
            dfs(i + 1, sub, total)
            
        dfs(0,[], 0)
        return res



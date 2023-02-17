class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(m, n, i):
            
            # Pointer has reached end of word so it is in the board
            if i == len(word):
                return True
            
            # Cases when you return
            # cell out of boundds or letter not eq to cell or cell already visited
            if m >= len(board) or n >= len(board[0]) or m < 0 or n < 0 or visited[m][n]:
                return False
            
            if word[i] != board[m][n]:
                return False
            
            visited[m][n] = True

            if backtrack(m + 1, n, i+1) or backtrack(m - 1, n, i+1) or backtrack(m, n + 1, i+1) or backtrack(m, n - 1, i+1):
                return True
            
            visited[m][n] = False
            return False

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for m in range(len(board)):
            for n in range(len(board[0])):
                if board[m][n] == word[0]:
                    if backtrack(m, n, 0):
                        return True
        
        return False

# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         ROWS, COLS = len(board), len(board[0])
#         path = set()

#         def dfs(r, c, i):
#             if i == len(word):
#                 return True
#             if (
#                 min(r, c) < 0
#                 or r >= ROWS
#                 or c >= COLS
#                 or word[i] != board[r][c]
#                 or (r, c) in path
#             ):
#                 return False
#             path.add((r, c))
#             res = (
#                 dfs(r + 1, c, i + 1)
#                 or dfs(r - 1, c, i + 1)
#                 or dfs(r, c + 1, i + 1)
#                 or dfs(r, c - 1, i + 1)
#             )
#             path.remove((r, c))
#             return res

#         # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
#         count = defaultdict(int, sum(map(Counter, board), Counter()))
#         if count[word[0]] > count[word[-1]]:
#             word = word[::-1]
            
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if dfs(r, c, 0):
#                     return True
#         return False

#     # O(n * m * 4^n)

        
        

            

            
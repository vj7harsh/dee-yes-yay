def robber(arr, n):
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    dp = [arr[0], max(arr[0], arr[1])]
    for i in range(2, n):
        dp.append(max(dp[i - 1], dp[i - 2] + arr[i]))
    return dp[-1]

def searchwords(grid, words):
    def search(board, word):
        n = len(board)
        m = len(board[0])
        dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def backtrack(i, r, c, seen):
            if i == len(word):
                return True
            for x, y in dir:
                r1 = r + x
                c1 = c + y
                if r1 in range(n) and c1 in range(m) and (r1, c1) not in seen:
                    if board[r1][c1] == word[i]:
                        seen.add((r1, c1))
                        if backtrack(i + 1, r1, c1, seen):
                            return True
                        seen.remove((r1, c1))
            return False
        
        for r in range(n):
            for c in range(m):
                if board[r][c] == word[0] and backtrack(1, r, c, {(r, c)}):
                    return True
        return False   
         
    ans = []
    for w in words:
        if search(grid, w):
            ans.append("Yes")
        else:
            ans.append("No")



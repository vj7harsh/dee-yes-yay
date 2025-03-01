class Backtrack:
    def permutate(n):
        ## premutations of n integrers 1 to n to form unique int
        ans = []
        def backtrack(curr):
            if len(curr) == n:
                ans.append("".join(curr))
            for i in range(1, n + 1):
                if i not in curr:
                    curr.append(i)
                    backtrack(curr)
                    curr.pop()
        backtrack([])
        return ans

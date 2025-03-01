def matchnswipe(videoSequence, k):
    stack = []
    count = 0
    for v in videoSequence:
        if stack and stack[-1] == v:
            stack.pop()
            count += 1
        else:
            stack.append(v)
    return count % k + 1

from collections import Counter
def maximumLikes(prediction):    
    freq = Counter(prediction)
    sorted_trends = sorted(freq.keys())
    n = len(sorted_trends)
    if n == 0:
        return 0
    if n == 1:
        return freq[sorted_trends[0]] * sorted_trends[0]
    dp = [0] * n
    dp[0] = freq[sorted_trends[0]] * sorted_trends[0]
    
    for i in range(1, n):
        trend = sorted_trends[i]
        likes = freq[trend] * trend
        
        if sorted_trends[i] == sorted_trends[i - 1] + 1:
            dp[i] = max(dp[i - 1], likes + (dp[i - 2] if i > 1 else 0))
        else:
            dp[i] = dp[i - 1] + likes  
        dp[i]

    MOD = 10**9 + 7
    return dp[-1] % MOD
from collections import defaultdict, deque
def rateLimit(times, addresses, limit, window):
    requests = defaultdict(deque)
    n = len(times)
    ans = []

    for i in range(n):
        ip = addresses[i]
        current_time = times[i]

        while requests[ip] and (requests[ip][0] + window < current_time):
            requests[ip].popleft()

        if len(requests[ip]) >= limit:
            ans.append(0)
        else:
            requests[ip].append(current_time)
            ans.append(1)

    return ans

# times1 = [1, 2, 3, 4, 5, 6]
# addresses1 = ["A", "A", "A", "A", "A", "A"]
# limit1 = 2
# window1 = 2
# print(f"Test 1 (Empty inputs): {rateLimit(times1, addresses1, limit1, window1)}") # Expected: []


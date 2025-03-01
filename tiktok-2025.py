def minAdditionalLatency(n, latency):
    from collections import defaultdict

    tree = defaultdict(list)
    for i in range(1, n): 
        parent = (i - 1) // 2 
        tree[parent].append((i, latency[i - 1])) 
    total_increment = 0

    def dfs(node):
        nonlocal total_increment
        if node not in tree:
            return 0
        
        max_latency = 0
        child_latencies = []

        for child, edge_latency in tree[node]:
            child_latency = dfs(child) + edge_latency 
            child_latencies.append(child_latency)
            max_latency = max(max_latency, child_latency)
        
        for child_latency in child_latencies:
            total_increment += max_latency - child_latency
        return max_latency
    dfs(0)

    return total_increment

def getMaxReview(s):
    l, r =  1, 1 
    ml , mr = l, r
    prefix = []
    for c in s:
        if len(prefix) == 0:
            if c == '0':
                prefix.append(-1)
            else:
                prefix.append(1)
        else:
            prefix.append(prefix[-1] + 1 if c == '1' else -1)
    
    for i in range(1, len(prefix)):
        if prefix[i] > 0 :
            r = i
        else:
            l = i + 1
            r = l
        if prefix[r] - prefix[l - 1] > prefix[mr] - prefix[ml - 1]:
            ml, mr = l, r        

    if mr < len(prefix) - 1:
        return -1 * prefix[ml - 1] + prefix[mr] - prefix[ml -1] + -1 * (prefix[-1] - prefix[mr + 1])
    else:
        return -1 * prefix[ml - 1] + prefix[mr] - prefix[ml -1]


def main():
    s = "1100111"    
    print(getMaxReview(s))
main()



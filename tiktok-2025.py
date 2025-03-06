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

from collections import defaultdict
import heapq
def maxConnectionsVerified(frm, to, n, unverified):
    unverified = set(unverified)
    parent = {i: i for i in range(1, n + 1)}
    rank = {i: 0 for i in range(1, n + 1)}
    total_possible = 0
    given_edges = len(frm)

    def find(u):
        if u != parent[u]:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        up = find(u)
        vp = find(v)
        if up != vp:
            if rank[up] > rank[vp]:
                parent[vp] = up
            elif rank[up] < rank[vp]:
                parent[up] = vp
            else:
                parent[vp] = up
                rank[up] += 1

    for u, v in zip(frm, to):
        union(u, v)
    
    clusters = defaultdict(list)
    cluster_status = defaultdict(bool)
    for i in range(1, n + 1):
        p = find(i)
        clusters[p].append(i)
        if i in unverified:
            cluster_status[p] = True

    unverified_clusters = []
    verified_cluster = []

    for p, c in clusters.items():
        if cluster_status[p]:
            heapq.heappush(unverified_clusters, -len(c))
        else:
            verified_cluster.extend(c)
    
    unv = -heapq.heappop(unverified_clusters)
    ver = len(verified_cluster)

    total_possible += ((unv + ver) * (unv + ver - 1)) / 2

    while unverified_clusters:
        l = -heapq.heappop(unverified_clusters)
        total_possible += ((l) * (l- 1)) / 2
    
    return total_possible - given_edges

def main():
    s = "1100111"    
    print(getMaxReview(s))
main()



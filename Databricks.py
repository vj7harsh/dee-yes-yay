import heapq
def getminCostToTavel(neighbors, fuel, start, destination, distance):
    h = []
    heapq.heappush(h, (0, fuel[start], start))
    seen = {}
    while(h):
        cost, fuel_price, curr_node = heapq.heappop(h)
        if curr_node == destination:
            return cost
        if (curr_node, fuel_price) in seen:
            continue
        seen[(curr_node, fuel_price)] = True
        fuel_price = min(fuel_price, fuel[curr_node])
        for n in neighbors[curr_node]:
            if (n, fuel_price) not in seen:
                heapq.heappush(h , (cost + (distance[curr_node][n] / fuel_price), fuel_price, n))
    return -1

        
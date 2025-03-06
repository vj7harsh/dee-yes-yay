from collections import defaultdict
class Visa:
    def gettriplets(queries, diff):
        trips = 0 
        ans = []
        count = defaultdict(int)
        def gettriplets(n):
            return count[n - diff] * count[n + diff] + count[n - diff] * count[n - 2 * diff] + count[n + diff] * count[n + 2 * diff]  
        for q in queries:
            n = int(q[1:])
            if q[0] == '+':
                count[n] += 1
                trips += gettriplets(n)
                ans.append(trips)
            else:
                trips -= gettriplets(n) * count[n]
                ans.append(trips)
                count[n] = 0
        return ans
    
    def getLexoSmall(s):
        return ""


queries = ["+10", "+20", "+30", "-20"]
diff = 10

result = Visa.gettriplets(queries, diff)
print(result)



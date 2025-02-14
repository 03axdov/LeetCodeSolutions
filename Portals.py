from typing import List
# Write any import statements here

dic = {}
portals = {}
seen = set()

def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
    for row in range(R):
        for col in range(C):
            if G[row][col] == "S":
                res = dfs(G, row, col)
                if res == float("inf"): return -1
                return res

def dfs(G, row, col):
    global dic
    global seen
    
    if (row, col) in seen: return float("inf")
    if row < 0 or row >= len(G): return float("inf")
    if col < 0 or col >= len(G[0]): return float("inf")
    if G[row][col] == "#": return float("inf")
    if G[row][col] == "E":
        return 0
    
    seen.add((row, col))
    res = []
    if (row, col) in dic.keys():
        return 1 + dic[(row, col)]
    if G[row][col] != "." and G[row][col] in portals.keys():
        dic[(row, col)] = 1 + portals[G[row][col]]
        return dic[(row, col)]
    
    res.append(dfs(G, row-1, col))
    res.append(dfs(G, row+1, col))
    res.append(dfs(G, row, col-1))
    res.append(dfs(G, row, col+1))
        
    dic[(row, col)] = 1 + min(res)
    if G[row][col] != ".":
        portals[G[row][col]] = dic[(row, col)]

    return dic[(row, col)]


R = 3
C = 4
G = ["a.Sa"
    "####"
    "Eb.b"]
print(getSecondsRequired(R,C,G))
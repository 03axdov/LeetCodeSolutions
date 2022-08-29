def findCircleNum(isConnected):
    output = 0
    visited = set()

    def dfs(i):
        for t, city in enumerate(isConnected[i]):
            if city == 1 and t not in visited:
                visited.add(t)
                dfs(t)

    for i in range(len(isConnected)):
        if i not in visited:
            dfs(i)
            output += 1
    return output


print(findCircleNum(
[[1,0,0,1],
[0,1,1,0],
[0,1,1,1],
[1,0,1,1]]))
def equationsPossible(equations) -> bool:
    unionFind = {}

    def find(x):
        unionFind.setdefault(x, x)
        if x != unionFind[x]:
            unionFind[x] = find(unionFind[x])
        return unionFind[x]

    def union(x, y):
        unionFind[find(x)] = find(y)
        
    for e in equations:
        if e[1] == '=':
            union(e[0], e[-1])
    for e in equations:
        if e[1] == '!':
            if find(e[0]) == find(e[-1]):
                return False
    return True


print(equationsPossible(["a==b","b!=c","c==a"]))
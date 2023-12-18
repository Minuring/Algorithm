MST = [
    [1],
    [0, 3],
    [3],
    [1, 2, 4, 5],
    [3],
    [3, 6],
    [5]
]
n = len(MST)

visited = [False for _ in range(n)]
path = []

def dfs(v):
    visited[v] = True
    path.append(v)
    for dest in MST[v]:
        if not visited[dest]:
            dfs(dest)
            path.append(v)

dfs(0)
result = [0]
for p in path:
    if p not in result:
        result.append(p)
result.append(0)

print(result)
import sys; input=sys.stdin.readline
V, E = map(int,input().split())

edges = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
edges.sort(key=lambda x:x[2])

roots = [i for i in range(0, V+1)]
count = 0

def find(v):
    if roots[v] != v:
        roots[v] = find(roots[v])
    return roots[v]

for u,v,w in edges:
    uRoot, vRoot = find(u), find(v)
    if uRoot != vRoot :
        count += w

        minV, maxV = min(uRoot,vRoot), max(uRoot,vRoot)
        roots[maxV] = minV

print(count)
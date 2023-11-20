import sys; input=sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    # a에서 b로 가는 가중치 c의 간선
    G[a].append([b,c])

dist = [float('inf')] * (N+1)
start, dist[1] = 1, 0
minusCycle = False
for cnt in range(N):
    for i in range(1,N+1):
        for j in G[i]:
            u, v, w = i, j[0], j[1]
            if dist[u] != float('inf') and dist[v] > dist[u] + w :
                dist[v] = dist[u] + w
                if cnt == N-1 :
                    minusCycle = True


if minusCycle :
    print(-1)
else :
    print("\n".join(list(map(str,dist[2:]))).replace("inf","-1"))
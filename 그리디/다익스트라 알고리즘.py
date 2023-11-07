import sys; input=sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
G = [[] for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int,input().split())
    G[u].append([v,w]) #u,v,w

dist = [float('inf') for _ in range(V+1)]

def dijkstra(s):
    visited = [False for _ in range(V+1)]
    # 시작 정점은 거리는 0, 기방문 상태로 시작
    dist[s] = 0
    visited[s] = True

    # 최소거리 정점 찾기
    for i in range(1, V+1):
        min_dist = float('inf')
        min_vertex = i
        for j in range(1, V+1):
            if not visited[j] and dist[j] < min_dist:
                min_dist = dist[j]
                min_vertex = j

    # 최소거리 정점으로부터 연결된 노드들 간의 거리 갱신
        for v,w in G[min_vertex]:
            if dist[v] > dist[min_vertex]+w:
                dist[v] = dist[min_vertex]+w

dijkstra(start)
print('\n'.join(list(map(str,dist[1:]))))


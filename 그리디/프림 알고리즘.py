V, E = map(int, input().split()) #정점 수, 간선 수
G = [[] for _ in range(V)]
for _ in range(E) :
  u, v, w = map(int, input().split())
  G[u].append([v,w])
  G[v].append([u,w])

sum = 0 #MST의 가중치 총합
included = [False for _ in range(V)]
dist = [float('inf') for _ in range(V)]
connected_to = [-1 for _ in range(V)]

dist[0] = 0
for u in range(0, V):

    min_vertex = -1 #index
    min_dist = float('inf')

    for k in range(0, V) : #정점 U에서 연결된 최소 거리의 정점 탐색
        if not included[k] and min_dist > dist[k] :
            min_dist = dist[k]
            min_vertex = k

    sum += min_dist
    included[min_vertex] = True

    #(정점 U에서 가장 인접한)
    #min_vertex와 연결되는 정점들간 거리 갱신
    #갱신을 해야 다음 단계(u+1)에서 제대로 알고리즘 수행 가능
    for v,w in G[min_vertex] :
        if not included[v] and w < dist[v] :
            dist[v] = w
            connected_to[v] = min_vertex

print('MST 가중치 : ', sum)
print('DIST : ', dist)
print('Connected_to : ', end='')
for i in range(1,V) :
    print(f'(%d-%d)'%(i,connected_to[i]), end='')
#입력 그래프의 인접 행렬 만들기
g = [[0,1,0,1,1,1],
     [1,0,1,1,0,1],
     [0,1,0,1,0,0],
     [1,1,1,0,1,0],
     [1,0,0,1,0,1],
     [1,1,0,0,1,0]]
n = len(g)
K = 3
color = [-1 for i in range(n)]  #각 정점의 색을 -1로 초기화

def valid(i): #i번째 정점이 이웃한 점과 같은 색이 아닌지 ?
    for v in range(len(g[i])):
        if g[i][v] == 1 and color[v ] == color[i] :
            return False
    return True

def coloring(i) :
    if i == n :
        print("정답 ", color)
        return

    usedColors = [color[j] for j in range(n) if g[i][j] == 1 and color[j] != -1]

    for c in range(K): #최대 정점개수만큼의 색깔이 필요할 수 있음
        if c not in usedColors:
            color[i] = c #c번째 색깔로 우선 칠해보고
            if valid(i): #이웃점과 색이 안 겹치면
                coloring(i+1) #다음 점 색칠
            else: continue # (색칠 안되면 다른색깔 해보고)

    #다 안되면 i번째 정점을 색칠할 수가 없는거
    return
    # else : continue


coloring(0)
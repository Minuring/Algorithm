
a = [['문학회', 9.0, 11.0], ['지역봉사회', 9.0, 12.5], ['서예회', 13.0, 14.5],
     ['바둑회', 14.0, 17.0], ['미술회', 11.0, 14.0], ['사진회', 9.0, 11.0],
     ['음악회', 15.0, 16.5], ['창조회', 15.0, 16.5], ['독서회', 11.0, 12.5],
     ['토론회', 13.0, 14.5]]

#1. 그래프로 만든다.
G = [[0 for i in range(len(a))] for _ in range(len(a))]

for i in range(len(a)):
     for j in range(i+1,len(a)):
          if a[i][1] < a[j][2] and a[i][2] > a[j][1]:
               G[i][j] = G[j][i] = 1

K = 3
room = [-1] * len(a)
def valid(v):
     for i in range(len(G)):
          if G[v][i] == 1 and room[v] == room[i]:
               return False
     return True

flag = False
def dfs(v):
     global flag
     if v == len(a):
          flag = True
          print("탐색한 해 : ", room)
          return

     for r in range(K):
          room[v] = r
          if valid(v) :
               dfs(v+1)

dfs(0)
if not flag:
     print("해가 없습니다")
N = int(input())
row = [0 for i in range(N)]
visited = [False for i in range(N)]

depth, count = 0, 0


def dfs(r):  # r번째 행에 퀸을 놓는다.
    global count

    if r == N:
        count += 1
        return

    for c in range(N):
        if visited[c]: continue

        row[r] = c  # r번째행 c열에 퀸을 놓아 보고
        # print(row)
        if valid(r):  # r번째행에 둔 퀸이 조건에 부합하면
            visited[c] = True
            dfs(r + 1)
            visited[c] = False


def valid(r):  # r번째 행에 둔 퀸이 조건에 부합하는 지
    for i in range(r):  # 현재 놓으려는 행(r번째) 이전 행들에 대해
        # row[i] : i번째 행에는 퀸을 몇 번째 열에 뒀는지?
        if row[i] == row[r] or (abs(i - r) == abs(row[i] - row[r])):  # i번째 행에서 퀸의 열 위치 == 현재 놓으려는 열 위치
            return False
        # r : 0~N , row[r] : 0~N번째행에서 놓은 퀸의 열번호.
        # c : 체크하고있는(놓으려는) 열 번호. 행은 자동으로 늘려가는 중
        # row[r] == c : 열번호 같음
        # 행번호 : depth가 곧 행번호. 안겹침
        # 대각선 : row[r]과 row[c]의 차 == r과 c의 차 => 겹침
    return True


dfs(0)
print(count)
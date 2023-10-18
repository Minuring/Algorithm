'''
맨 처음 수업의 종료시간을 먼저 힙에 삽입하고 시작한다.
times는 시작시간 순 정렬 되어있으므로, 반복문에서 시작시간이 빠른 순으로
비교하게된다.
파이썬 heapq는 최소힙이므로 최소값이 들어있으므로 heapq의 루트에는
"항상" 개설된 강의실 중 가장 빨리 끝난 시간이 들어있다.

따라서 times의 시작시간을 순회하며 heapq의 루트와 비교하고, 전자가 크거나 같으면
강의실 개설을 안 해도되고, 아니면 강의실을 개설한다.
'''
import heapq
import sys

N = int(sys.stdin.readline())
times = []
for _ in range(N) :
    tmp = list(map(int, sys.stdin.readline().split()))
    times.append(tmp)
times.sort()

ans = []
heapq.heappush(ans, times[0][1]) #가장 먼저 시작하는 수업을 넣고 시작

for i in range(1, N) : #첫 수업 제외한 수업의 개수만큼
    if times[i][0] >= ans[0] :
        heapq.heappop(ans)

    heapq.heappush(ans, times[i][1])

print(len(ans))
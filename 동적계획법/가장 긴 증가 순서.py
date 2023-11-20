def makeAdjList(S) :
    G = []
    for i in range(len(S)):
        adjL = []
        for j in range(i):
            if S[i] > S[j] :
                adjL.append(j)
        G.append(adjL)
    return G


def getLongestIncreasingSeq(S) :
    G = makeAdjList(S)
    N = len(S)
    length = [1] * N
    previous = [-1] * N

    for i in range(1, N) :
        if len(G[i]) > 0 :
            maxLength = -1
            for v in G[i]:
                if length[v] > maxLength :
                    maxLength = length[v]
                    previous[i] = v
                    # i번째 숫자는 v번째 숫자 다음이다.
                    # i번째 숫자 이전 숫자는 v번째 숫자이다.
            length[i] = maxLength + 1

    print(max(length))
    k, res = length.index(max(length)), []
    while k != -1 :
        res.insert(0,S[k])
        k = previous[k]
    print(' '.join(list(map(str,res))))
    return

N = int(input())
L = list(map(int, input().split()))
getLongestIncreasingSeq(L)
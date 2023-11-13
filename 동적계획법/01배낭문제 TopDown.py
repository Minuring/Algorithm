import sys; input = sys.stdin.readline

N, K = map(int, input().split())

products = []
for i in range(N) :
    tup = tuple(map(int, input().split()))
    #각 물건의 무게 W, 가치 V  --  (W, V)
    products.append(tup)

memo = [[-1 for _ in range(K+1)] for _ in range(N+1)]
def solve(n, k) :
    if n==0 or k<=0 :
        return 0

    if memo[n][k] != -1 :
        return memo[n][k]

    w, v = products[n-1]
    if w > k :
        memo[n][k] = solve(n-1, k)
    else :
        memo[n][k] = max( solve(n-1,k), solve(n-1,k-w)+v )
    return memo[n][k]

print(solve(N,K))
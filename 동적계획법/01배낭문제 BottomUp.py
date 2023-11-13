import sys; input = sys.stdin.readline

N, K = map(int, input().split())

products = []
for i in range(N) :
    tup = tuple(map(int, input().split()))
    #각 물건의 무게 W, 가치 V  --  (W, V)
    products.append(tup)
def solve(K):
    dp = [0]*(K+1)

    for w,v in products:
        for i in range(K, w-1, -1) :
            dp[i] = max(dp[i], dp[i-w]+v)

    return dp[K]

print(solve(K))
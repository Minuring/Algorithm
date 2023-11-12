def solve_BottomUp(coin, money) :
    dp = [-1]*(money+1)
    dp[0] = 0

    for m in range(1, money+1) :
        dp[m] = float('inf')
        for i in coin:
            if m >= i :
                dp[m] = min(dp[m], 1+dp[m-i])

    return dp[money]

print(solve_BottomUp([5,10],25))
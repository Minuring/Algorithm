def solve_TopDown(coins, money, memo):
    if money == 0 :
        return 0
    elif money < 0 :
        return float('inf')
    elif memo[money] != -1 :
        return memo[money]

    count = float('inf')
    for i in coins:
        count = min(count, 1 + solve_TopDown(coins, money - i, memo))

    memo[money] = count
    return memo[money]

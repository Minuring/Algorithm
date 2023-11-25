source = list(input())
target = list(input())

dp = [[0] * (len(source)+1) for _ in range((len(target)+1))]
for i in range(len(source)+1) : dp[0][i] = i
for i in range(len(target)+1) : dp[i][0] = i

for i in range(1,len(target)+1) :
    for j in range(1,len(source)+1) :

        if target[i-1] == source[j-1] :
            dp[i][j] = dp[i-1][j-1]
        else :
            replace = dp[i-1][j-1] + 1
            add = dp[i][j-1] + 1
            delete = dp[i-1][j] + 1

            dp[i][j] = min(replace,add,delete)

#print('\n'.join(list(map(str,dp))))
print(dp[len(target)][len(source)])
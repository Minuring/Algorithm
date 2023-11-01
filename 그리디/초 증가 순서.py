S = list(map(int,input("초 증가 순서 입력 : ").split()))
S.sort()
K = int(input("K 입력 : "))

ans = []
i = len(S)
while K > 0 :
    i -= 1
    if S[i] > K : continue
    K -= S[i]
    ans.append(S[i])

print(f'선택된 수 : {ans} , 합 : {sum(ans)}')
S = [-1, 1110, 1008, 1250, 1006] # S[0]은 사용하지 않음
K = 2500
n = len(S)
epsilon = 0.4
delta = epsilon/(2*n)

def major_number(v,delta):
    v.sort()
    majorN, result = v[0] , []
    for i in range(len(v)):
        if majorN < v[i] <= majorN*(1 + delta):
            continue
        result.append(v[i])
        majorN = v[i]
    return result


T = [[0] for _ in range(n)]

for i in range(1, n):
    T[i] = list( set(T[i-1]) | set([S[i]+k for k in T[i-1]]) ) # A, T 합병
    T[i] = major_number(T[i],delta)
    T[i] = [k for k in T[i] if k <= K]

print(f'마지막 숫자 리스트 : {T[n-1]}')
print(f'근사해 : {max(T[n-1])}')
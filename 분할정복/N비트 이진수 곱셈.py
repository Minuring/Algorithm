def product(a, b, n):
    if n == 1:
        return a * b

    # a와 b를 상위 절반과 하위 절반으로 분할
    a_High = a >> (n // 2)
    a_Low = a % 2**(n//2)
    b_High = b >> (n // 2)
    b_Low = b % 2**(n//2)

    # 재귀적으로 곱셈 수행
    m1 = product(a_High, b_High, n // 2)
    m2 = product((a_High + a_Low), (b_High + b_Low), n // 2)
    m3 = product(a_Low, b_Low, n // 2)

    # 결과 계산
    result = (2 ** n) * m1 + (2 ** (n // 2)) * (m2 - m1 - m3) + m3

    return result

a = int(input("A 입력 : "),2)
b = int(input("B 입력 : "),2)
n = len(bin(a))-2

result = product(a, b, n)
print(bin(result))  # 2진수로 결과 출력

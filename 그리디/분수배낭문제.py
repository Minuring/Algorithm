Name = ['A','B','C']
Price = [150, 100, 150]
Weight = [10, 20, 5]
Capacity = 20

def ft(Name, Price, Weight, Capacity) :
    L = list(zip(Name, Price, Weight))
    S, maxP = [], 0
    L.sort(key=lambda k : k[1]/k[2], reverse=True)
    # lambda k에서 k == L[i] , k[1]/k[2] == Price/Weight 무게 대비 가격

    # 무게 대비 가격순 정렬되었으므로 P/W가 큰 순으로 iterate
    for name, price, weight in L :
        if weight > Capacity : # 무게 > 용량 : 분할해야하는 경우
            S.append((name, Capacity)) # weight 중 Capacity만큼 
            maxP += Capacity * price / weight # Capacity X 무게당가격
            break
        S.append((name, weight))
        Capacity -= weight
        maxP += price

    return maxP, S


print(ft(Name, Price, Weight, Capacity))
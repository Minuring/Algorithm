BIN_SIZE = 10
item = [7,5,6,4,2,3,7,5]
n = len(item)

bins = [0]
for i in range(n):

    flag = False
    for binIndex in range(len(bins)):
        if bins[binIndex] + item[i] <= BIN_SIZE :
            bins[binIndex] += item[i]
            flag = True
            print(f'{item[i]}를 {binIndex}번째 통에 넣음 [ {bins[binIndex]} / 10 ]')
            break

    if not flag:
        bins.append(item[i])
        print(f'{item[i]}를 {len(bins)-1}번째 통에 넣음 [ {bins[-1]} / 10 ]')

print(bins)

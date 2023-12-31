# 분할정복
- [K번째 작은 수](./K번째%20작은%20수.py)

<pre>퀵정렬처럼 피벗을 구한다.
<b>피벗</b>은 현재 입력크기만큼의 배열에서 <b>피벗의 인덱스 +1번째</b>로
작은 원소이다.
한 번의 단계(분할)마다 피벗을 기준으로 어느 한 쪽을 탐색할 필요가 없어진다.

최악의 경우 : 퀵정렬과같이 치우친 분할을 할 때 O(N^2)이다.
        T(N) = T(N-1) + N = T(N-2) + (N-1) + ··· + T(1) + (N-1) + (N-2) + ··· + 1 = O(N^2)

최선의 경우 : 피벗이 매 번 절반씩 분할한다면 O(N)이다.
평균의 경우 : 피벗을 랜덤하게 설정하면 확률적으로 2번에 한 번은 균등하게
            분할한다. 따라서 O(2N) = O(N)이다.
        T(N) = T(N/2) + N = T(N/4) + N/2 + N = ··· = T(1) + 1/2^k + N/(2^k-1) + ··· + 1 = O(N) 
</pre>

- [N비트 이진수 곱셈](./N비트%20이진수%20곱셈.py)

<pre>A x B (2진수) 
A와 B를 A_H, A_L, B_H, B_L (2/N비트씩) 로 분할한다.
M1 = A_H * A_L
M2 = (A_H + A_L) * (B_H + B_L)
M3 = B_H * B_L
곱셈 결과는 <b>(2^N * M1) + (2^(N/2) * (M2-M1-M3)) + M3</b> 이다.

한 번의 단계마다 3번의 분할(M1~M3)이 이루어지며, 비트 수를 1/2씩 쪼개어가므로,
log2^N번의 단계가 지나면 비트수가 1이된다.
즉 단계마다 3번의 분할을 하며, log2^N단계를 거치게 되므로
시간복잡도는 O(N^(log2^3)) 이다.
</pre>

- [퀵 정렬](./QuickSort.py)

<pre>피벗을 정한다. (본 코드는 항상 가장 왼쪽 값으로 설정)
피벗보다 작은 원소들은 피벗의 왼쪽으로, 피벗보다 큰 원소들은 피벗의 오른쪽으로 옮긴다.
피벗을 기준으로 왼쪽과 오른쪽 부분을 각각 퀵정렬한다.

피벗을 정하고 왼쪽, 오른쪽으로 원소들을 옮기는 과정은 O(N) 시간이 걸린다. <partition>
한 번의 단계마다 partition( O(N) ) + 왼쪽, 오른쪽 분할을 한다.
최악의 경우 : 피벗을 기준으로 <b>한 쪽으로 치우친 분할</b>을 하게 된 경우
(가장 작은 수 또는 가장 큰 수를 피벗으로 선정했을 때) 분할 후 배열의 크기는 1씩 줄어들게 되므로
최종적으로 O(N^2)이다.

최선의 경우 : 중앙값을 피벗으로 선정해 균등하게 분할되면,
log2^N번의 분할 * 분할마다의 partition( O(N) )으로 O(NlogN)이다.
</pre>

- [이진 탐색](./이진탐색.py)

<pre>탐색하려는 배열은 정렬되어있어야한다.
정렬되어있지 않으면, 반드시 Key값을 찾는다는 보장을 할 수 없다.

탐색범위의 왼쪽과 오른쪽이 엇갈리면 탐색에 실패. 배열에 Key값이 없다.

현재 배열에서 중간 위치의 값과 Key값을 비교한다.
Key값이 더 크면 : 오른쪽 절반에서 이진탐색한다.
Key값이 더 작으면 : 왼쪽 절반에서 이진탐색한다.

한 번의 단계마다 탐색 범위가 1/2씩 줄어들기 때문에, log2^N번의 단계를 거치면 탐색 결과를 얻는다.
따라서 시간복잡도는 O(log2^N)이다.
</pre>

- [합병 정렬](./합병정렬.py)

<pre>배열의 중간을 기준으로 양쪽으로 크기가 1이하가 될 때까지 분할한다.
분할된 왼쪽과 오른쪽을 결합한다. 이 과정에서 아래와 같이 정렬이 이루어진다.
- 임시 리스트에 순차적으로 왼쪽, 오른쪽 배열에서 가장 작은값을 삽입한다.
- 임시 리스트를 원래 리스트에 대입한다.

한 번의 단계마다 부문제의 크기는 2/N이 되고, 결합과정은 O(N)의 시간이 걸린다.
즉 log2^N번의 단계를 거치고, 각 단계마다 결합하는 데 O(N)의 시간이 걸린다.
T(N) = 2*T(N/2) + O(N) = 4*T(N/4)+O(N) + O(N) = ··· = log2^N * O(N)
따라서 최선, 평균, 최악의 경우 모두 O(NlogN)이다.
</pre>

- [최근접 이웃 점](./최근접%20이웃%20점.py)

<pre>먼저 입력 좌표들을 X좌표를 기준으로 정렬한다.
정렬된 X좌표의 중앙값 (m). (=X좌표상 중앙에 있는 점)을 기준으로 왼쪽, 오른쪽으로 분할한다.
분할된 왼쪽, 오른쪽 영역에서 재귀적으로 최근접 이웃 점을 찾는다.
왼쪽 영역에서의 최근접 점간 거리 = pL, 오른쪽 영역에서의 최근접 점간 거리 = pR이라하면,
pL과 pR을 비교해 최근접 이웃 점 사이의 거리 p를 얻는다.

두 영역이 합쳐지고 나면 <b>중앙 영역에 최근접 이웃점이 있었을 수 있다.</b>

X좌표의 중앙값 (양쪽으로 나누었던 기준 점) m에서부터 X좌표 상에서 양쪽으로 p만큼의 거리 내의
점들을 후보군 리스트에 추가한다. (이 과정을 위해 알고리즘 시작 전 X좌표를 기준으로 정렬했었다.)

후보군 리스트의 점들을 Y좌표 기준으로 정렬한다.
Y좌표가 가장 작은 점부터, 후보군들 내에서 비교하면서 후보군 내에서 최소거리를 찾는다.

후보군 내의 최소거리 (=왼쪽,오른쪽 분할에 의해 못 찾았던 중앙 영역의 최소 거리)와,
p(=왼쪽, 오른쪽 영역 중 최소거리) 중 작은 값이 <strong>입력 점들 중 최근접 이웃 점</strong>이다.


먼저 X좌표 정렬에서 O(NlogN)의 시간이 소요된다.
(분할과정) 한 번의 단계마다 N/2씩 분할하며,
(취합과정) 중앙 영역의 최소거리(후보군 내 최소거리)를 찾는 작업도 O(NlogN)이 걸린다.
    (Y좌표정렬 NlogN, 각각 비교)
따라서, log2^N번의 층수, 각 층수마다 NlogN의 시간이 걸리므로
총 시간복잡도는 O( N*(log2^N)^2 ) 이다.

</pre>
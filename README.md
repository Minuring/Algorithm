# Algorithm
알고리즘 공부
<hr>
<strong>TODO</strong>

12/04

시간복잡도 정확히 알기<br>

합이 k되는 숫자 구현해보기 (방식차이: 숫자를 선택/포기)<br>

아래코드(nQueens) 분석하기<br>g

<pre>
def solve_n_queens(n):
count = 0
MASK = (1 << n) - 1

def count_solutions(left, col, right):
    nonlocal count
    if col == MASK:
        count += 1
        return
    free_positions = ~(left | col | right) & MASK
    while free_positions:
        curr_pos = -free_positions & free_positions
        free_positions -= curr_pos
        count_solutions((left | curr_pos) << 1, col | curr_pos, (right | curr_pos) >> 1)

count_solutions(0, 0, 0)
return count
print(solve_n_queens(int(input())))
</pre>
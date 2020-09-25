import sys
from math import ceil, log

N, K, M = map(int, sys.stdin.readline().rstrip().split(" "))

numbers = []
for _ in range(N) :
    numbers.append(int(sys.stdin.readline().rstrip()))

# init
tree = [0] * (4*N)

def init(start, end, node) :
    if start == end :
        tree[node] = numbers[start]
        return tree[node]

    mid = (start+end)//2

    tree[node] = (init(start,mid,node*2) * init(mid+1,end,node*2+1)) % 1000000007
    return tree[node]

init(0,N-1,1)

def update(start, end, idx, node_num, val) :
    # diff는 변경되는 값으로 생기는 값의 차이 . 여기서는 비율?
    if not (start <= idx <= end):
        return tree[node_num]

    if start == end :
        tree[node_num] = val
        return tree[node_num]


    mid = (start+end)//2

    tree[node_num] = ( update(start, mid, idx, node_num*2, val) * update(mid+1, end, idx, node_num*2+1, val) ) % 1000000007
    return tree[node_num]

# find section
def query(node_left, node_right,left, right, node_num) :
    # print(node_left, node_right, left, right, node_num)
    if left > node_right or right < node_left :
        return 1

    if left <= node_left and right >= node_right :
        # node_left ~ node_rigt까지 해당하는 부분을 반환
        return tree[node_num]

    mid = (node_left+node_right)//2

    return ( query(node_left, mid, left, right, node_num*2) * query(mid+1, node_right, left, right,  node_num*2+1) ) % 1000000007
#
for _ in range(M+K) :
    a,b,c = map(int, sys.stdin.readline().rstrip().split(" "))

    if a == 1 :
        update(0, N - 1, b - 1, 1, c)
        numbers[b-1] = c
    else :
        print(int(query(0, N-1, b-1, c-1, 1)))

# 여기서는 update를 해당 값까지 가서 바꾼 뒤 다시 계산을 한다.

# 그러나 부분 합에서는 바뀐 값과의 차이만을 더해 주며 갱신하는 방법도 있다. <-- 이게 더 빠를 듯.
# 하지만 이 문제에서는 0이 되는 부분때문에 구현에 귀찮음이..

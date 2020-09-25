# 시간 초과 에러남.. 책에 있는 코드 변환한건데..

# class RMQ :
#
#     def __init__(self, array):
#         self.N = len(array)
#         self.rangeMin = [None for _ in range(4*self.N)]
#         self.array = array
#         self.makeTree(0, self.N-1, 1)
#
#     def makeTree(self, left, right, node):
#         if left == right :
#             self.rangeMin[node] = self.array[left]
#             return self.rangeMin[node]
#
#         mid = (left+right)//2
#         leftMin = self.makeTree( left, mid, node*2)
#         rightMin = self.makeTree(mid+1, right, node*2+1)
#
#         self.rangeMin[node] = min(leftMin, rightMin)
#         return self.rangeMin[node]
#
#     def query(self, left,right):
#         return self.query_rec(left,right,1,0,self.N-1)
#
#     def query_rec(self, left, right, node, nodeLeft, nodeRight):
#
#         if right < nodeLeft or nodeRight < left :
#             return float('inf')
#
#         if left <= nodeLeft and nodeRight <= right :
#             return self.rangeMin[node]
#
#         mid = (nodeLeft+nodeRight)//2
#
#         return min(self.query_rec(left,right,node*2,nodeLeft,mid),
#                   self.query_rec(left,right,node*2+1,mid+1,nodeRight))
#
#     def update(self, index, value):
#         return self.update_rec(index, value, 1, 0, self.N-1)
#
#     def update_rec(self, index, value, node, nodeLeft, nodeRight):
#
#         if index < nodeLeft or nodeRight < index :
#             return self.rangeMin[node]
#
#         if nodeLeft == nodeRight :
#             self.rangeMin[node] = value
#             return self.rangeMin[node]
#
#         mid = (nodeLeft+nodeRight)//2
#
#         self.rangeMin[node] = min( self.update_rec(index, value, node*2, nodeLeft, mid),
#                                    self.update_rec(index, value, node*2+1, mid+1, nodeRight) )
#

def init(start, end, node) :
    if start == end :
        tree[node] = [numbers[start]]
        return [tree[node]

    mid = (start+end)//2

    left = init(start, mid, node * 2)
    right = init(mid + 1, end, node * 2 + 1)
    now = sorted(left+right)

    tree[node] = [now[0],now[1]]
    return tree[node]

# def update(start, end, idx, node_num, val) :
#     # diff는 변경되는 값으로 생기는 값의 차이 . 여기서는 비율?
#     if not (start <= idx <= end):
#         return tree[node_num]
#
#     if start == end :
#         tree[node_num] = val
#         return tree[node_num]
#
#
#     mid = (start+end)//2
#
#     tree[node_num] = ( update(start, mid, idx, node_num*2, val) * update(mid+1, end, idx, node_num*2+1, val) ) % 1000000007
#     return tree[node_num]

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

# init(0,N-1,1)
# for _ in range(M+K) :
#     a,b,c = map(int, sys.stdin.readline().rstrip().split(" "))
#
#     if a == 1 :
#         update(0, N - 1, b - 1, 1, c)
#         numbers[b-1] = c
#     else :
#         print(int(query(0, N-1, b-1, c-1, 1)))



import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T) :
    N, Q = map(int, sys.stdin.readline().rstrip().split(" "))
    numbers= list(map(int,sys.stdin.readline().rstrip().split()))
    # minus_signs = [-e for e in signs]
    tree = [0] * (4*N)
    init(0,N-1,1)

    print(tree)


    # for _ in range(Q) :
    #     start,end = map(int, sys.stdin.readline().rstrip().split(" "))
    #     paths.append((start, end))

    # rmq_plus = RMQ(signs)
    # rmq_minus = RMQ(minus_signs)
    #
    # for path in paths :
    #     print(-rmq_minus.query(path[0], path[1]) - rmq_plus.query(path[0], path[1]))

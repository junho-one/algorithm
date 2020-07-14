# 시간 초과 에러남.. 책에 있는 코드 변환한건데..

class RMQ :

    def __init__(self, array):
        self.N = len(array)
        self.rangeMin = [None for _ in range(4*self.N)]
        self.array = array
        self.makeTree(0, self.N-1, 1)

    def makeTree(self, left, right, node):
        if left == right :
            self.rangeMin[node] = self.array[left]
            return self.rangeMin[node]

        mid = (left+right)//2
        leftMin = self.makeTree( left, mid, node*2)
        rightMin = self.makeTree(mid+1, right, node*2+1)

        self.rangeMin[node] = min(leftMin, rightMin)
        return self.rangeMin[node]

    def query(self, left,right):
        return self.query_rec(left,right,1,0,self.N-1)

    def query_rec(self, left, right, node, nodeLeft, nodeRight):

        if right < nodeLeft or nodeRight < left :
            return float('inf')

        if left <= nodeLeft and nodeRight <= right :
            return self.rangeMin[node]

        mid = (nodeLeft+nodeRight)//2

        return min(self.query_rec(left,right,node*2,nodeLeft,mid),
                  self.query_rec(left,right,node*2+1,mid+1,nodeRight))

    def update(self, index, value):
        return self.update_rec(index, value, 1, 0, self.N-1)

    def update_rec(self, index, value, node, nodeLeft, nodeRight):

        if index < nodeLeft or nodeRight < index :
            return self.rangeMin[node]

        if nodeLeft == nodeRight :
            self.rangeMin[node] = value
            return self.rangeMin[node]

        mid = (nodeLeft+nodeRight)//2

        self.rangeMin[node] = min( self.update_rec(index, value, node*2, nodeLeft, mid),
                                   self.update_rec(index, value, node*2+1, mid+1, nodeRight) )


import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T) :
    N, Q = map(int, sys.stdin.readline().rstrip().split(" "))
    signs = list(map(int,sys.stdin.readline().rstrip().split()))
    minus_signs = [-e for e in signs]
    paths = []

    for _ in range(Q) :
        start,end = map(int, sys.stdin.readline().rstrip().split(" "))
        paths.append((start, end))

    rmq_plus = RMQ(signs)
    rmq_minus = RMQ(minus_signs)

    for path in paths :
        print(-rmq_minus.query(path[0], path[1]) - rmq_plus.query(path[0], path[1]))

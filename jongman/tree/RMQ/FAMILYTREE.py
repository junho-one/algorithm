# 런타임 에러가 난다.. 찾아봐야함

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

def traverser(num,depth) :

    preOrder.append(num)
    if not depths[num] :
        depths[num] = depth

    for child in childs[num] :
        traverser(child, depth+1)
        preOrder.append(num)

import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T) :
    N, Q = map(int, sys.stdin.readline().rstrip().split(" "))
    fathers = list(map(int, sys.stdin.readline().rstrip().split()))
    childs = [[] for _ in range(N)]
    depths = [None for _ in range(N)]

    preOrder = []
    paths = []
    for _ in range(Q) :
        a,b = map(int, sys.stdin.readline().rstrip().split(" "))
        paths.append((a,b))

    for num, father in enumerate(fathers,start=1) :
        childs[father].append(num)

    traverser(0,0)

    preOrder_depth = [0 for _ in range(len(preOrder))]
    # 노드 번호가 메겨진 preOrder를 노드 깊이가 메겨진 preOrder로 변환
    for i in range(len(preOrder)) :
        preOrder_depth[i] = depths[preOrder[i]]

    rmq = RMQ(preOrder_depth)

    for start,end in paths :
        try :
            s_i = preOrder.index(start)
            e_i = preOrder[s_i:].index(end) + s_i
        except ValueError :
            e_i = preOrder.index(start)
            s_i = preOrder[e_i:].index(end) + s_i

        LCA_depth = rmq.query(s_i,e_i)
        s_depth = depths[preOrder[s_i]]
        e_depth = depths[preOrder[e_i]]

        print(s_depth + e_depth - 2*LCA_depth)



# 구간트리는 배열에서 어떤 구간에 최소값이 무엇인지 찾을 때 잘 쓰인다.
# 여기서는 어떤 구간에서 최소 공통 조상이 무엇인지를 찾는 것 ( 최소공통 조상이 항상 두 숫자 사이에 존재한다는 가정하에 가능 + 특정 조건이 있고 (최소, 최빈 등등) )
# 사실 전위순회한 식에서 두 숫자 사이에는 있는 최소 깊이를 가진 노드가 항상 최소 공통 조상이다.

# 구

# 트리 전위순회를 통해 최소 공통 조상을 찾을 수 있다.

# 트리 순회를 하려면 트리를 만들 필요가 없다 그냥 child를 담고 있는 배열만 있으면 가능 !!!

# preOrder에서 나오는 두 수 사이에는 최소조상이 존재한다.
# preOrder [1 2 3 4 6 4 3 5 7 ] 이라면 1 4 사이에 있는 2,3 중에 최소 조상이 있다.
# 2,3중 어느게 최소 조상인지 모른다. 그렇기에 각 번호에 대한 depth를 구한 뒤 depth가 가장 작은게 최소 조상이 된다.

# preOrder하면서 번호를 치환함으로써 항상 조상이 자손보다 숫자가 더 작게 할 수 있다.
# 전위순회는 항상 루트부터 돌고 서브트리를 도니 당연한 결과



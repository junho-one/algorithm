import sys
import math

class Node :
    def __init__(self, x,y,r):
        self.x = x
        self.y = y
        self.r = r
        self.child = []

    def isIn(self, node):

        distance = math.sqrt( (self.x - node.x)**2 + (self.y - node.y)**2 )
        # print(node.x, node.y, self.x, self.y)
        # print(distance, self.r)
        if distance < node.r :
            return True
        else :
            return False

    def addChild(self, node):
        self.child.append(node)


class Tree :

    def __init__(self) :
        self.root = None
        self.distance = 0


    def add(self, node) :
        if self.root :
            self.go(self.root, node)
        else :
            self.root = node


    def go(self, root, node):

        for child in root.child :
            if node.isIn(child) :
                self.go(child, node)
                return True

        root.addChild(node)


    def maxDistance(self):
        self.maxDepth(self.root)


    def maxDepth(self, node):
        # node를 root로 하는 트리의 최대 높이,
        # 이 트리 안에서 노드간 최대 거리를 구함

        if not node.child :
            return 1

        depths = []
        maxDepth = 1
        for child in node.child :
            sub_depth = self.maxDepth(child)
            maxDepth = max(maxDepth, sub_depth+1)

            depths.append(sub_depth)

        if len(depths) > 1 :
            depths = sorted(depths, reverse=True)
            self.distance = max(self.distance, depths[0] + depths[1])
        else :
            self.distance = max(self.distance, depths[0])

        return maxDepth


T = int(sys.stdin.readline().rstrip())

for _ in range(T) :
    N = int(sys.stdin.readline().rstrip())

    fortress = []
    for _ in range(N) :
        x,y,r = map(int, sys.stdin.readline().rstrip().split(" "))
        fortress.append( (x,y,r) )


    fortress = sorted(fortress, key = lambda x: -x[2])
    tree = Tree()
    for x,y,r in fortress :
        tree.add( Node(x,y,r) )

    tree.maxDistance()
    print(tree.distance)



# 한 요새가 들어왔을 때 현재 있는 요새들의 영역 안에 들어간다면 그 요새의 자식으로 들어가야 한다.
# 이를 재귀적으로 반복한다면 요새는 들어 갈 수 있으면서 가장 안에 있는 요새로 들어가게 된다.
# 트리를 만드는 과정에서 들어오는 노드의 순서는 다 만들어졌을 때 부모 노드부터 들어와야 한다.
# 만약 r이 큰 것부터 넣는다면 자식노드가 먼저 나올리는 없다.

# 트리를 만들어주고
# 노드간의 최대 거리를 구하면 된다.
# 이때 노드의 최대거리는 최대 높이를 가진 서브트리의 높이 합이 된다.

#         A
#      B  C  D   로  A를 루트로 하고 B,C,D를 서브트리로 가진다면
#     B,C,D 중 높이가 가장 높은 두개를 골라 합을 구하면 된다.

# 이때 서브트리가 하나라면 서브트리의 높이가 최대 거리가 된다.
# 재귀를 통해 모든 서브트리에 대해 수행해주면 최대 높이를 구할 수 있다.

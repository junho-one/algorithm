class Tree :
    def __init__(self, pre_list, ins_list):
        self.pres_list = pre_list
        self.ins_list = ins_list
        self.root_idx = 0

    def makePost(self):
        return self.findRoot(self.ins_list)

    def findRoot(self, ins):

        if not ins :
            return ""

        root_num = self.pres_list[self.root_idx]
        self.root_idx += 1
        ins_root_idx = ins.index(root_num)

        left_ins = ins[:ins_root_idx]
        right_ins = ins[ins_root_idx+1:]
    
        left = self.findRoot(left_ins)
        right = self.findRoot(right_ins)

        left = left + " " if left else left
        right = right + " " if right else right

        return left + right + str(root_num)

import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T) :
    N = int(sys.stdin.readline().rstrip())

    pres = list(map(int, sys.stdin.readline().rstrip().split()))
    ins = list(map(int,sys.stdin.readline().rstrip().split()))

    tree = Tree(pres, ins)
    print(tree.makePost())



# 전위순회식은 항상 루트를 먼저 돈다. 중위순회식은 항상 루트를 왼쪽 서브트리를 다 돌고 돈다.

#     x
#   y   z
# 순휘식은 움직이면서 항상 이런 모양의 노드를 만나게 된다.
# 그러면 전위식은 xyz, 중위식은 yxz, 후위식은 yzx이다.
# y와 z밑에 어떤 값들이 있는지 모르니 xy[?]z[?]  y[?]xz[?], y[?]z[?]x로 표현이 가능하다.
# x를 루트, y를 왼쪽 서브트리, z를 왼쪽 서브트리라고 보면 이 셋만 잘 나눌 수 있다면 위치를 재배열해 후위식을 만들 수 있다.

# 그렇다면 중위식에서는 항상 루트 번호 왼쪽은 왼쪽에 달린 서브트리고, 오른쪽은 오른쪽에 달린 서브트리가 된다.
# 전위식에서는 항상 루투를 먼저 도니까 나오는 번호가 항상 루트 번호를 의미한다.
# 전위식에서 현재 트리의 루트번호를 찾고 중위식을 통해 왼쪽 서브트리, 루트, 오른쪽 서브트리를 구한다.
# 각 서브트리에서 나온 값과 루트값을 잘 배치하면 후위식이 된다.

# 전위순회식에서 항상 루트값을 찾은다음 중위식에서 왼쪽 subtree의 값들과 오른쪽 subtree의 값들을 찾을 수 있다.
# 이렇게 찢다보면 트리가 순회하는 경로와 같은 경로로 찢어지게 되고, left값, right값, 루트값이 나오는데
# 후위식은 left, right, root 순으로 이동하니까 left값 + right값 + root값을 반환하면 그 트리의 후위식이 완성된다.

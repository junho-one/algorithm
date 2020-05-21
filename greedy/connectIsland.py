import heapq


# kruskal 알고리즘을 이용하면 풀림
# 가중치가 있는 무향그래프를 모두 잇는 최소 신장트리
def solution(n, costs):
    class DisjointSet:
        def __init__(self, n):
            self.data = list(range(n))
            self.size = n

        def find(self, index):
            return self.data[index]

        def check(self, x, y):
            x, y = self.find(x), self.find(y)

            if x == y:
                return False
            else:
                return True

        def union(self, x, y):
            x, y = self.find(x), self.find(y)

            if x == y:
                return

            for i in range(self.size):
                if self.find(i) == y:
                    self.data[i] = x

    answer = 0

    costs = sorted(costs, key=lambda x: x[2])
    disjoint = DisjointSet(n)

    for ver1, ver2, cost in costs:

        if disjoint.check(ver1, ver2):
            disjoint.union(ver1, ver2)
            answer += cost

    return answer


solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
    
import sys
import heapq

N, K = map(int, sys.stdin.readline().rstrip().split(" "))

jewerly = []
for _ in range(N) :
    M, V = map(int, sys.stdin.readline().rstrip().split(" "))
    jewerly.append((M,V))

bags = []
for _ in range(K) :
    bags.append(int(sys.stdin.readline().rstrip()))

remains = []

bags = sorted(bags)
jewerly = sorted(jewerly)

maxHeap = []

b_i = 0
j_i = 0
answer = 0
while b_i < K and j_i < N:

    if bags[b_i] >= jewerly[j_i][0] :
        weight, value = jewerly[j_i]
        heapq.heappush(maxHeap, -value)
        j_i += 1

    elif bags[b_i] < jewerly[j_i][0] :

        if maxHeap :
            maxValue = heapq.heappop(maxHeap)
            answer += -maxValue
        b_i += 1


while b_i < K and maxHeap:
    maxValue = heapq.heappop(maxHeap)
    answer += -maxValue
    b_i += 1

print(answer)

# M과 V가 모두 30만이길래 기준을 가방으로 잡던 보석으로 잡던 기준 아이템을 하나씩 채우는데 logN 이하의 시간이 걸려야 문제를 풀 수 있다.
# 둘다 무게를 오름차순으로 정렬한다. 그리고 두 리스트의 원소를 가리키는 bag_index와 jewerly_index로 0을 가리킨다.

# 만약 bag_index가 가리키는 가방의 무게가 jewerly_index가 가리키는 보석의 무게보다 작다면
# 가방은 이 보석 뒤에 있는 보석들은 넣을 수 없으므로 이 전에 있는 보석 중에 하나를 선택해야 한다.

# 가방이 자신보다 무게가 큰 보석을 만날 때까지 보석을 모두 maxHeap에 넣는다. 그리고 만났을 때 maxHeap에서 가장 무거운 보석을 꺼낸다면
# 가방은 자신이 담을 수 있는 가장 큰 무게의 보석을 담게 된다.

# 보석을 담은 후에는 bag_index를 하나 증가시켜 다음 가방에서 위와 같은 작업을 한다.
# 현재 가방이 담을 수 있는 무게는 은 이전 가방의 것보다 항상 크므로 maxHeap에 담겨져 있는 보석은 모두 담을 수 있다.
# 그리고 현재 가방이 담을 수 있는 보석을 모두 담은 후 maxHeap에서 꺼내는 작업을 반복하면 된다.


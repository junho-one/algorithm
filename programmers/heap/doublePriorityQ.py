import heapq


def solution(operations):

    minHeap = []
    maxHeap = []
    insert = 0
    deleteMax = 0
    deleteMin = 0

    for oper in operations:

        # minHeap과 maxHeap에 둘다 넣어줌
        if oper[0] == 'I':
            insert += 1
            heapq.heappush(minHeap, int(oper.split(" ")[1]))
            heapq.heappush(maxHeap, -int(oper.split(" ")[1]))

        # D 1이 들어오면 deleteMax 을 1 증가시키고 maxHeap에서 하나를 뺀다
        elif oper[-2:] == ' 1':
            deleteMax += 1
            if maxHeap :
                heapq.heappop(maxHeap)

        # D -1이 들어오면 deleteMin 을 1 증가시키고 minHeap에서 하나를 뺀다
        elif oper[-2:] == '-1':
            deleteMin += 1
            if minHeap :
                heapq.heappop(minHeap)

        # 만약 deleteMax와 deleteMin의 합과 insert가 갖다면 모든 원소가 지워진 상태이므로 힙을 초기화한다.
        # 만약 deleteMax와 deleteMin의 합이 insert보다 작다면 빈 힙을 지우는 행동을 한 것이므로 똑같이 초기화 해준다.
        if insert <= deleteMax+ deleteMin :
            minHeap = []
            maxHeap = []
            insert = 0
            deleteMin = 0
            deleteMax = 0

    # 힙 안에 값이 없으면 [0,0] 리턴
    if deleteMin + deleteMax >= insert :
        return [0,0]
    else :
        return [-heapq.heappop(maxHeap), heapq.heappop(minHeap)]


print(solution(['I 16','D 1']))
print(solution(['I 7','I 5','I -5','D -1']))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
print(solution([["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]]))
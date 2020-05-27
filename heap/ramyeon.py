import heapq

def solution(stock, dates, supplies, k):

    answer = 0
    dateIdx = 0
    heap = []

    # stock은 k일까지만 버티면 되기에 k보다 커지면 충분한 양을 공급받은 상태이므로 종료
    while stock < k :

        # 현재 stock으로 버틸 수 있는 날짜까지 공급받을 수 있는 supply를 maxHeap으로 저장한다.
        while dateIdx < len(dates):

            # 날짜가 현재 stock을 넘어가면 현 상태로는 이 supply를 받을 수 없기에 종료
            if dates[dateIdx] > stock:
                break
            # 가능한 날짜 안에 있는 supply는 담는다.
            heapq.heappush(heap, -supplies[dateIdx])
            dateIdx += 1

        # 모든 공급 받을 수 있는 날짜까지 supply를 담고 최대값을 뽑아 stock에 더한다.
        if heap:
            stock += -heapq.heappop(heap)
            answer += 1

    return answer

print(solution(4,[1,2,3,4],[1,1,1,1],6))
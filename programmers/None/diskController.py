# 프로그래머스 디스크 컨트롤러
import heapq

def solution(jobs):
    answer = 0
    jobs.sort()

    heap = [[jobs[0][1], jobs[0][0]]]

    idx = 1
    fullTime = 0
    while heap :
        cost, start = heapq.heappop(heap)

        if start <= fullTime :
            fullTime += cost
        else :
            fullTime = start + cost

        answer = answer + fullTime - start

        while idx < len(jobs) and jobs[idx][0] <= fullTime :
            heapq.heappush(heap, [jobs[idx][1], jobs[idx][0]])
            idx += 1

        if idx < len(jobs) and not heap :
            heapq.heappush(heap, [jobs[idx][1], jobs[idx][0]])
            idx += 1
        # 쌓인 job이 없고, 시간이 흐른 뒤 발생하는 job이 있을 때
        # heap에 아무것도 없으면 while문에서 탈출하니 넣어준다


    return answer // len(jobs)

print( solution([[0, 3], [1, 9], [2, 6]]) )
print( solution([[2, 6]]) )
print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]))

# 현재 시간보다 시작 시간이 작은 job들 중에서 수행 시간이 가작 작은 값부터 수행한다.
# 만약 밀린 일이 있으면 총 걸린시간은 현재까지 걸린 시간에 다음 작업의 수행 시간이고,
# 밀린 일이 없다면 총 걸린 시간은 다음 작업이 끝나는 시간이다.

import heapq


def solution(people, limit):
    answer = 0

    people = list(map(int, people))
    people = sorted(people, reverse=True)
    boats = []

    heapq.heappush(boats, people[0])

    # 가장 큰 사람부터 보트에 넣는다.
    for peo in people[1:]:

        minBoat = boats[0]

        # 사람이 탄 보트 중 최소 무게를 가진 보트와 현재 사람을 비교하여 합이 100보다 작으면 넣는다.
        if minBoat + peo <= limit:
            num = heapq.heappop(boats)
            # 이때 보트에 탈 수 있는 사람이 2명이 최대니까 더이상 보트에 사람이 탈 수 없게 큰 값을 넣는다.
            heapq.heappush(boats, num + 1000)
        else:
            # 탈 수 있는 보트가 없다면 새로운 보트에 사람을 태워 넣는다.
            heapq.heappush(boats, peo)

    return len(boats)


solution([40, 40, 40], 200)
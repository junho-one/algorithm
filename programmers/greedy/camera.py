# 한 카메라로 모두 감시할 수 있는 경로들이 있을 때, 카메라가 설치되어야 하는 범위는
# 들어온 경로중 가장 큰 시작점에서부터 가장 작은 끝점안에 카메라가 들어간다면 모든 경로를 감시할 수 있을 것이다.
# 현재 카메라가 설치될 수 있는 범위에서 감시가 안되는 경로는 새로운 감시카메라를 설치해 감시해야한다.

def solution(routes):
    answer = 0

    # 구간을 시작하는 수로 오름차순으로 정렬한다
    routes = sorted(routes, key=lambda x: (x[0], x[1]))

    # camCover는 현재 카메라가 단속할 수 있는 가장큰 값이다.
    possibleRange = routes[0][1]

    answer = 1

    for route in routes[1:]:

        # possibleRange를 현재 경로의 시작점과 비교한다. 현재 경로 시작점이 더 크다면
        # 현재 카메라로는 단속할 수 없는 범위기에 새로운 카메라를 추가한다. 그리고 possibleRange를 현재 경로의 끝나는 지점으로 한다.
        if possibleRange < route[0]:
            possibleRange = route[1]
            answer += 1

        # 현재 경로의 시작점이 더 작다면 possibleRange와 끝점을 비교하여 더 작은 값으로 대체한다.
        else:
            if possibleRange > route[1]:
                possibleRange = route[1]

    return answer


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
def solution(n, t, m, timetable):
    bus = 540 - t
    times = []
    for time in timetable:
        hour, minute = time.split(":")
        times.append(int(hour) * 60 + int(minute))

    times.sort()

    idx = 0
    riding = []
    for i in range(n):
        bus += t
        board = m

        while idx < len(times) and board > 0:
            if times[idx] <= bus:
                riding.append(times[idx])
                idx += 1
                board -= 1
            else:
                break

    if board > 0:
        time = bus

    elif board == 0:
        time = max(riding) - 1

    hour = str(time // 60)
    minute = str(time % 60)

    answer = hour.zfill(2) + ":" + minute.zfill(2)

    return answer


# print(solution(1,1,5,['08:00', '08:01', '08:02', '08:03']))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))


# bus가 오는 횟수 n만큼 돌면서 버스 도착시간을 체크한다.
# 버스 도착시간 보다 일찍 온 사람들은 태우고 (board -=1) 모든 배차가 끝날 때 까지 반복한다.
# 만약 board(마지막 버스에 남은 자리)가 0보다 크면 마지막 배차 시간에 가서 타면 된다.
# board가 0이라면 마지막 버스에 자리가 꽉 찼기에 마지막으로 탄 사람보다 1분 빨리 가면 된다.
# 버스에 탄 사람을 담은 배열 riding을 통해 마지막 탈 수 있는 자리를 기록한다.

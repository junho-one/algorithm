# 카카오 추석 트래픽

def solution(lines):
    answer = 0

    logs = []

    for log in lines:
        end, time = log[11:].split(" ")
        time = float(time[:-1])
        hour, min, sec = end.split(":")

        total = int(hour) * 3600
        total += int(min) * 60
        total += float(sec)
        total = int( total * 1000 )
        start = total - int(time * 1000 -1)

        logs.append((start, total))

    candidates = set()
    for start, end in logs :
        candidates.add((start,start+999))
        candidates.add((start-999,start))

    for start, end in candidates :
        cnt = 0

        for log in logs :
            if start <= log[0] <= end or start <= log[1] <= end :
                cnt += 1
            elif log[0] < start  and end < log[1] :
                cnt += 1
        answer = max(cnt, answer)
    return answer

#  처리량이 가장 많은 1초만 구하면 된다.
# 근데 처리량이 변화하는 시점은 하나의 데이터 처리가 시작하는 시점과 끝나는 시점이다.
# 이 중 끝나는 시점은 무조건 처리량은 줄어든다. 그러니 데이터가 시작하는 시점만 찾아보면 된다.

print( solution(['2016-09-15 01:00:04.002 2.0s', '2016-09-15 01:00:07.000 2s']) )
print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))

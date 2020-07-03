import sys
import bisect

# 1개
T = int(sys.stdin.readline().rstrip())

for _ in range(T) :

    N = int(sys.stdin.readline().rstrip())
    warm = list(map(int,sys.stdin.readline().rstrip().split()))
    eat = list(map(int,sys.stdin.readline().rstrip().split()))

    lunch_boxes = sorted( zip(warm,eat), key = lambda x : (-x[1],x[0]) )

    times = []
    total_warm = 0
    maxTime = 0
    for idx, box in enumerate(lunch_boxes) :

        total_warm += box[0]
        # times.append( total_warm + box[1] )
        maxTime = max(maxTime, total_warm + box[1])

    # print(sorted(times)[-1])
    print(maxTime)

# 먹는 일은 동시에 진행되지만, 전자레인지는 혼자 진행된다.
# 도시락을 데우는 데 걸리는 시간은 항상 일정하다.
# 데우는 시간 + 먹는 시간이 총 걸리는 시간인데 데우는 시간은 고정되어 있으니 먹는 시간을 줄여야 한다.
# 그렇다면 먹는데 오래 걸리는 도시락을 가장 먼저 해치우면 시간이 감소될 것이다.
# 먹는 시간이 가장 긴 것을 먼저 처리하면 최적의 해인가?

# 먹는데 걸리는 시간이 x라는 최적해가 있다.
#
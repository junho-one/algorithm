import sys
import bisect

# 1개
T = int(sys.stdin.readline().rstrip())

for _ in range(T) :
    N = int(sys.stdin.readline().rstrip())
    A = list(map(int,sys.stdin.readline().rstrip().split()))
    B = list(map(int,sys.stdin.readline().rstrip().split()))

    A = sorted(A)
    B = sorted(B)
    idx_A = 0
    idx_B = 0

    while idx_B < len(B) :

        if A[idx_A] <= B[idx_B] :
            idx_A += 1
            idx_B += 1

        else :
            idx_B += 1

    print(idx_A)


# 항상 우리팀이 적팀의 상대보다 근소한 레이팅 차이로 이기기만 하면 최대 승이 나온다. 즉 상대 점수보다 높은 애들 중 가장 점수가 낮은 애를 내보내면 된다.
# 우리팀과 적팀의 레이팅을 오름차순으로 정렬해놓고 서로 레이팅이 낮은 애들부터 비교한다.
# 상대팀과 우리팀의 레이팅을 비교해서 만약 우리팀의 레이팅이 더 높다면 이 친구를 출전시켜 승을 챙긴다.
# 하지만 상대 레이팅이 더 높다면 이 친구는 이길 수 있는 사람이 없으니 맨뒤로 보내 가장 높은 적과 싸우게 한다.
# 그렇게 비교하며 우리팀 리스트를 다 돌면 끝난다.

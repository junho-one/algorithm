import sys
import heapq

# 1개
T = int(sys.stdin.readline().rstrip())

for _ in range(T) :

    N = int(sys.stdin.readline().rstrip())
    lengths = list(map(int,sys.stdin.readline().rstrip().split()))

    heapq.heapify(lengths)
    answer = 0

    for _ in range(N-1) :
        a = heapq.heappop(lengths)
        b = heapq.heappop(lengths)

        heapq.heappush(lengths, a+b)
        answer += a+b

    print(answer)


# 계속해서 길이가 작은 두 글자를 합치면 최소가 된다.  == 허프만 코드
# 합치는데는 두 문자열 길이의 합만큼 걸리니까 계속해서 더해준다.

# 문자열 두개가 병합될 때마다 두 길이의 합이 계속 더해져서 전체 비용이 정해진다.

# 전체 반복문 횟수는
# a,b,c,d 길이가 있고 a - b - c - d 순으로 합쳐진다고 가정하면
# a + b => a+b
# (a+b) + c => a+b+c
# (a+b+c) + d => a+b+c+d
# 3a+3b+2+d가 총 횟수가 된다.
# 이 수식은 글자 수가 n개일 때로도 일반화가 가능하다.
# 즉 일찍 합쳐지면 더 많은 병합과정을 거친다. 병합과정에서 나오는 연산량은 문자열의 길이에 비례하므로
# 일찍합쳐지는 문자열이 작다면 더 적은 연산량이 나온다.

# 그렇다면 앞의 문자열에 작은 수가 와야함이 보인다.





# 가장 작은 문자열 a,b가 있다.
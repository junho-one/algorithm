import sys
sys.setrecursionlimit(10**6)

def calculate_level(S) :

    # level 1 test
    if len(set(S)) == 1 :
        return 1

    # level 2 test
    prev = S[0]-1
    for val in S :
        if val - prev != 1 :
            break
        prev = val
    else :
        return 2

    prev = S[-1] - 1
    for val in reversed(S) :
        if val - prev != 1 :
            break
        prev = val
    else :
        return 2

    # level 3 test
    twos = [S[0], S[1]]
    idx = False
    for val in S :
        if twos[idx] != val :
            break
        idx = ~idx
    else :
        return 4


    # level 4 test
    diff = S[1] - S[0]
    prev = S[0] - diff
    for val in S :
        if val - prev != diff :
            break
        prev = val
    else :
        return 5

    return 10

def pi(start) :

    if N == start :
        return 0

    if dp[start] :
        return dp[start]


    ret = float('inf')
    # 만약 start 가 N-2로 들어와 남은 문자열 길이가 2이라면, if문을 통과 못해서 return 값이 INF가 될 것이고 다른 재귀 min값 비교 과정에서 사라질 것이다
    # start +i 가 N보다 크면 재귀도 돌리지 말고 N== start면 return 0을해서 끝냄 (문자열 끝까지 다 간 상황)
    for i in range(3,6) :
        if start + i <= N :
            ret = min(ret, pi(start+i) + calculate_level(nums[start:start+i]))

    dp[start] = ret

    return dp[start]

# 1개
T = int(sys.stdin.readline().rstrip())
answer = []
for _ in range(T) :
    nums = list(map(int,list(sys.stdin.readline().rstrip())))
    N = len(nums)
    dp = [ None for _ in range(N)]

    answer.append(pi(0))

for ans in answer :
    print(ans)



# 문제를 보면 인덱스 0부터 시작해서 끝까지 가는 문자열의 최소 난이도를 찾는 문제이다.
# 그렇다면 인덱스 3부터 시작해서 끝까지 가는 문자열의 최소 난이도, 인덱스 4부터 시작해서 끝까지 가는 문자열의 최소 난이도 등의 부분 문제로 쪼갤 수 있다.
# 인덱스 x가 주어졌을 때 x 앞부분의 문자열 최소 난이도와 뒷부분의 문자열 최소 난이도는 별개의 값이다. => 최적 부분 구조
# base case를 주어지는 인덱스가 문자열 길이 값과 같아 지는 순간 즉, 문자열 끝까지 도달한 상황으로 한다.
# 그리고 문자열이 들어가면 난이도를 반환해주는 함수를 만들어 난이도 계산을 해주고 최소값을 구해준다

# 문제 오답 이유
# 시간초과가 나는데 clacluate_level 함수를 잘 못짜서 그런건지, 파이썬이라 느려서 안되는건지 잘 모르겠다.
# slice의 시간복잡도는 잘리는 원소의 개수에 비례하므로 3~5이다. 그럼 calculate_level을 상수시간으로 둬도 상관없지 않나?
# 재귀에서의 시간복잡도는 3개씪 생기니까 3^N ??    -> 그러나 dp니까 N??



import sys

def lis(start) :

    # 기저사례 모든 수열을 탐색했으니 0 반환
    if start == N :
        return 0

    if dp[start] :
        return dp[start]

    now = A[start]
    ret = now

    for idx in range(start+1,N) :
        # 현재 인덱스에 해당하는 값보다 큰 값으로만 접근
        if now < A[idx] :
            # 현재 인덱스 값 + idx에서 부터 시작한 증가 수열의 최대값
            ret = max(ret, lis(idx)+now)

    # ( 현재 인덱스 값 + idx에서 부터 시작한 증가 수열의 최대값 )들의 최대값 == 현재 인덱스에서 부터 시작한 증가 수열의 최대값
    dp[start] = ret

    return dp[start]


N = int(sys.stdin.readline().rstrip())
A = list(map(int,sys.stdin.readline().rstrip().split()))

# 인덱스 0에 수열의 최소값을 넣어준다.
A.insert(0,-1)
N += 1

maxLen = 0

dp = [None for _ in range(len(A))]

# 수열의 최소값이 포함된 결과이므로 최소값을 다시 빼준다.
print(lis(0)+1)

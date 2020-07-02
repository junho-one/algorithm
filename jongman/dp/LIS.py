
def LIS(seq, idx) :
    print(seq, idx)
    if idx == len(A) :
        # print(seq)
        return True

    if not seq or seq[-1] < A[idx] :
        seq.append(A[idx])
        LIS(seq, idx + 1)
        seq.pop()

    LIS(seq, idx +1)



import sys
sys.setrecursionlimit(10**6)

# 1개
T = int(sys.stdin.readline().rstrip())



def lis(start) :

    if dp[start] :
        return dp[start]

    now = A[start]
    ret = 1
    for idx in range(start+1,N) :
        if now < A[idx] :
            ret = max(ret, lis(idx)+1)

    dp[start] = ret

    return dp[start]

answer = []
for _ in range(T) :

    N = int(sys.stdin.readline().rstrip())

    A = list(map(int,sys.stdin.readline().rstrip().split()))


    maxLen = 0

    # lis함수는 시작 위치가 정해준다. 0번째가 첫 위치가 아닐 수도 있으니 모든 문자열 인덱스에서 한번씩 시작할 수 있도록 한다.
    dp = [None for _ in range(501)]

    for i in range(N) :
        maxLen = max(maxLen, lis(i))
    answer.append(maxLen)

for ans in answer :
    print(ans)
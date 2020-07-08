
import sys

T = int(sys.stdin.readline().rstrip())
QWE = 0
def polynomio(now, block) :

    if block == 0 :
        return 1

    if dp[now][block] != -1 :
        return dp[now][block]

    cnt = 0

    for i in range(1, block+1) :
        cnt += polynomio(i, block-i) * (now+i-1)
        cnt %= 10000000
    dp[now][block] = cnt
    return cnt


for _ in range(T) :
    N = int(sys.stdin.readline().rstrip())

    dp = [ [ -1 for _ in range(N+1)] for _ in range(N+1) ]

    answer = 0
    for i in range(1, N+1) :
        answer = ( answer + polynomio(i,N-i) ) % 10000000

    print(answer % 10000000)
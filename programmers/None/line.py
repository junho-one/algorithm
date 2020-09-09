# 프로그래머스 줄서는 방법
dp = [None] * 22
def fac(i):

    if dp[i] :
        return dp[i]

    if i == 0 or i == 1:
        return 1
    else:
        dp[i] = fac(i - 1) * i
        return dp[i]


def solution(n, k):
    answer = []

    factorials = []
    for i in range(1, n + 1):
        factorials.append(fac(i))

    factorials.reverse()

    for idx, fact in enumerate(factorials) :
        if k > fact :
            break

    answer = list(range(1,n+1))
    base = idx-1
    cand = answer[base:]
    # print("CAND", cand)
    tmp = []
    while len(cand) > 1 :
        val = k//factorials[idx]
        rem = k%factorials[idx]
        # print(k, factorials[idx], val, rem, tmp)
        if rem == 0 :
            val -= 1

        k = rem
        idx += 1
        tmp.append(cand.pop(val))

    tmp = tmp + cand

    answer[base:] = tmp

    return answer

print(solution(3, 1))

# k번째 순서를 각 위치에 팩토리얼 값을 통해 구할 수 있다.
# 만약 [1,2,3,4] 인 수열이 있으면, 각 위치별 팩토리얼 값은 [4!, 3!, 2!, 1!]이 된다.
# 순서가 3이라면, 3!도 못넘기니 앞에서 부터 1번째 자리 수는 1이 된다. [1,x,x,x]
# 만약 순서가 7이라면 3!을 넘기니까 7 / 3! = 1이 되고, 1번째 자리 수는 index가 1인 수 즉 [2,x,x,x]가 된다.

# 또한 최대 20!인데, 순서가 15번째라면 앞의 수는 1,2,3,4,5 .... 일 것이고, 뒤에 몇자리에서만 순서교체가 일어날 것이다.
# base는 순서 값으로 인해 이미 정해진 수열의 앞부분을 가리킨다.
# base부터 뒷부분만 위와 같은 계산을 통해 순서를 정하면 된다.

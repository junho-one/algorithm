import sys

# N개
a,b = map(float, sys.stdin.readline().rstrip().split(" "))

def multiply_list(A,B,dp_A, dp_B) :

    if len(A) < len(B) :
        return multiply_list(B,A,dp_B,dp_A)

    dp = dp_A + dp_B

    result = [0 for _ in range(len(A) + len(B))]

    # 기본 곱셈
    for b_i, b in enumerate(B) :
        for a_i, a in enumerate(A) :
            result[b_i+a_i] += b*a

    # 자리수 올림
    for idx, val in enumerate(result) :

        if val >= 10 :
            up = val // 10
            remain = val % 10

            result[idx] = remain
            result[idx+1] += up

    # 밑의 코드는 00.3432 같은 수를 처리해주기 위해

    # 소수점 위의 숫자가 다 0이 아니라면
    if any(result[dp:]) :
        # 최상단의 숫자가 0이면 뺴주기
        for val in reversed(result) :
            if val == 0 :
                result.pop()
            else :
                break
    else :
        # 0을 하나만 남기기
        result = result[:dp] + [0]

    return result, dp


def power(base, exp) :
    if exp == 1 :
        return base, dp_base

    if exp % 2 != 0 :
        res, dp_res = power(base, exp - 1)
        return multiply_list(res, base,dp_res, dp_base)

    else :
        half, dp_half = power(base, exp//2)
        return multiply_list(half,half,dp_half,dp_half)

A = []
dp_base = 0
a = str(a)

for idx, s in enumerate(reversed(a)) :
    if s != '.' :
        A.append(int(s))
    else :
        dp_base = idx

ans, dp_ans = power(A,b)
ans = list(map(str, ans))
answer = "".join(ans[:dp_ans]) +"."+ "".join(ans[dp_ans:])

print(answer[::-1])




# 그냥 float 곱셈으로 값을 구해보니 소수점 밑자리에서 오차가 생긴다.
# 정교한 곱셈을 하기 위해 값들을 리스트화 한 뒤 일일이 계산해주었다.
# 곱셈의 시간복잡도는 n^2을 따른다.
# 곱셈의 개수는 매번 logN을 따른다
# 거듭제곱 개수가 최대 100번이니 최대 log100 ~ 6번 정도만 재귀를 돈다.
# a의 최대 자리수는 11개이다. 11개를 100번 곱해도 1100자리의 숫자이고 이는 충분히 제한시간 안에 풀 수 있다.


# 틀린 이유
# 리스트를 이용한 소수점 곱셈에서 최상위 자리의 수가 0일 가능성이 있다.
# 이 경우에는 0을 제거해줘야 한다. 하지만 00.0432와 같은 숫자의 경우
# 0을 모두 제거하는게 아닌 소수점 윗자리로 하나의 0만 남기게 해야한다.
# 이부분을 간과하고 0을 모두 제거하는 코드를 짜서 틀렸었다.

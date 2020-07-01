# karatsu로 개선해야함

import sys

# 1개
N = int(sys.stdin.readline().rstrip())

def multiply(A,B) :

    result = [0 for _ in range(len(A) + len(B))]

    # 기본 곱셈
    for b_i, b in enumerate(B) :
        for a_i, a in enumerate(A) :
            result[b_i+a_i] += b*a

    return result

for _ in range(N) :

    str_mem = sys.stdin.readline().rstrip()
    str_fan = sys.stdin.readline().rstrip()

    members = list(map(lambda x: 1 if x == 'M' else 0, list(str_mem)))
    fans = list(map(lambda x: 1 if x == 'M' else 0, list(str_fan)))
    members = list(reversed(members))
    # fans = list(reversed(fans))
    len_mem = len(members)
    len_fan = len(fans)

    res = multiply(fans,members)
    ans = 0
    for i in range(len_mem-1, len_fan) :
        if res[i] == 0 :
            ans += 1

    print(ans)


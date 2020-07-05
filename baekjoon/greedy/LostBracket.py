# 백준 1541 잃어버린 괄호

import sys

def lostBracket(expr):
    plus_stack = []
    answer = []

    while expr:

        element = expr.pop(0)

        if element == '-':
            answer.append(sum(plus_stack))
            answer.append('-')
            plus_stack = []
        elif element.isdecimal():
            plus_stack.append(int(element))

        if not expr:
            answer.append(sum(plus_stack))

    ans = answer[0]
    for i in range(2, len(answer), 2):
        ans -= answer[i]

    return ans

# 백준 답 코드
S = sys.stdin.readline().rstrip()
oper = ['+','-']

num = ""
expr = []

for s in S:
    if s in oper:
        expr.append(num)
        expr.append(s)
        num = ""
    else:
        num += s
expr.append(num)

print(lostBracket(expr))

# 테스트 케이스를 임의로 만들어 테스트 해보는 코드
# import random
# plus_stack = []
# for _ in range(10) :
#
#     expr = []
#     for _ in range(random.randrange(5,21,2)) :
#         expr.append(str(random.randrange(1,100)))
#
#     for i in range(1,len(expr),2) :
#         expr[i] = random.choice(['+','-'])
#
#     print(expr)
#     print(lostBracket(expr))

# re.split("\+|-", S)
# print(re.split("\D", S))


# 몇개의 예제를 만들어 풀어보니 -가 나오면 뒤에 나오는 수를 최대로 만들고 - 연산을 맨 마지막에 해주면 된다.
# a + b - d + c - q + e 가 있다면 -가 두번 나온다.
# - 뒤에 수인 d+c를 해줘서 최대값을 만들고 다음 -의 뒤에 있는 수인 q+e를 해줘서 최대값을 만든 뒤 마지막에 -연산을 해주면 된다.

# 코드로 생각해보면 list를 처음부터 돌면서 숫자나 '+'가 나오면 배열에 넣어둔다.
# 그러다 -가 나오면 배열에 넣어둔 값을 모두 더한 뒤 최종 배열에 넣고 '-'도 최종 배열에 넣는다
# 이를 반복하여 식에서 더하기 연산을 다 해준 뒤 최종 배열에 있는 값을 이용해 빼기 연산을 처리해준다.



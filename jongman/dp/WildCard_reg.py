import sys
import re

# 1개
N = int(sys.stdin.readline().rstrip())

answer = []

for _ in range(N) :

    wild_card = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    strings = []

    wild_card = wild_card.replace("*",".*").replace("?",".")

    for _ in range(n) :
        strings.append(sys.stdin.readline().rstrip())


    answer = []

    for string in strings :
        p = re.compile(wild_card)
        matched = p.match(string)

        if matched and matched.group() ==  string :
            answer.append(string)

    answer = sorted(answer)
    for ans in answer:
        print(ans)
# 3
# he?p
# 3
# help
# heap
# helpp
# *p*
# 3
# help
# papa
# hello
# *bb*
# 1
# babbbc





# 문제를 어렵게 만드는 부분은 *이다.
# *에 해당하는 글자가 몇글자인지 마주한 순간에는 알 수가 없다.
# 그렇기에 앞의 문자열이 잘 매치되다가 *가 나온 순간 wild_card의 *다음에 나오는 문자열과
# string의 현재 인덱스에서부터 만들 수 있는 모든 문자열과 매칭 함수를 돌려 완전탐색하면 된다.
# 예를 들어 wild card : "tr*qw" 이고, string : "trqqeettqw" 라면
# *를 마주한 순간 string의 인덱스는 2로 q일 것이다. 이때 *가 몇개의 문자열에 해당하는지 모르니까 다 만들어 본다
# qqeettqw, qeettqw, eettqw, ettqw, ttqw, tqw, qw, w


# 틀린 이유
# 재귀 함수를 어떻게 짜야하는지 감이 오질 않았다.
# 문자열을 하나하나 비교해가면서 한번에 끝내려는 방법을 구상하다가
# wild card : "t*qw*t" , string : "tqw11111qwt" 와 같은 문자열이 나오면
# qw에 매칭되는 위치가 앞의 qw인지 뒤의 qw인지 판단할 수 없을 것이라고 생각하고 포기했다.


# 중복으로 발생되는 영역이 없어서 memoization이 사용 안될 것 같은데 어디서 쓰는거지?



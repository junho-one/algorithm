import sys

# 1개
N = int(sys.stdin.readline().rstrip())

def match(w_idx, s_idx) :

    if dp[w_idx][s_idx] != -1 :
        return dp[w_idx][s_idx]

    while w_idx < len_wild and s_idx < len_str and (wild_card[w_idx] == string[s_idx] or wild_card[w_idx] == '?') :
        s_idx += 1
        w_idx += 1

    if w_idx == len_wild  :
        dp[w_idx][s_idx] = (s_idx == len_str)
        return dp[w_idx][s_idx]


    if wild_card[w_idx] is '*' :

        for i in range(s_idx, len_str+1) :
            # w_idx가 wild_card를 넘어가버리는 상황 (*p*일때 w_ixd+1가 가서 len_wild에 해당하는 값이 다음 인자로 넘어감)
            # 그래서 이부분이 맞는지 틀리는지는 다음 재귀의 w_idx == len_wild부분에서 판단이 된다.
            # 그렇기에 s_idx도 len_str까지 가는 부분까지 포함시켜 range를 만들었다.

            if match(w_idx+1, i) :
                dp[w_idx][s_idx] = True
                return dp[w_idx][s_idx]


    dp[w_idx][s_idx] = False
    return dp[w_idx][s_idx]

    # return False

answer = []

for _ in range(N) :

    wild_card = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    strings = []

    for _ in range(n) :
        strings.append(sys.stdin.readline().rstrip())

    ans = []
    for string in strings :
        len_wild = len(wild_card)
        len_str = len(string)
        dp = [[-1 for _ in range(110)] for _ in range(110)]
        if match(0,0) :
            ans.append(string)

    answer.extend(sorted(ans))


for str in answer :
    print(str)

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



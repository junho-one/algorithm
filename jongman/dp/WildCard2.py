# import sys
#
# # 1개
# N = int(sys.stdin.readline().rstrip())
#
# def match(w_idx, s_idx) :
#
#     if dp[w_idx][s_idx] :
#         print(w_idx, s_idx)
#         return dp[w_idx][s_idx]
#
#     if w_idx < len_wild and s_idx < len_str and (wild_card[w_idx] == string[s_idx] or wild_card[w_idx] == '?') :
#         dp[w_idx][s_idx] = match(w_idx+1, s_idx+1)
#         return dp[w_idx][s_idx]
#
#     if w_idx == len_wild  :
#         dp[w_idx][s_idx] = (s_idx == len_str)
#         return dp[w_idx][s_idx]
#
#
#     if wild_card[w_idx] is '*' :
#
#         if match(w_idx+1, s_idx) or ( s_idx < len_str and match(w_idx, s_idx+1)) :
#             dp[w_idx][s_idx] = True
#             return True
#
#     dp[w_idx][s_idx] = False
#     return dp[w_idx][s_idx]
#
#     # return False
#
# def wildcard_exhaustive(pattern, word):
#
#     len_p, len_w = len(pattern), len(word) # 각 문자열의 길이를 구한다.
#     nth = 0  			           # 확인할 문자의 위치 변수. 0으로 초기화한다.
#
#     if dp[len_p][len_w] == -1:
#         return dp[len_p][len_w]
#
#     # 첫 번째 조건
#     while nth < len_p and nth < len_w and (pattern[nth] == '?' or pattern[nth] == word[nth]):
#         nth += 1
#
#     # 두 번째 조건
#     if len_p == nth:
#         return nth == len_w
#
#     # 네 번째 조건
#     if pattern[nth] == '*':
#         skip = 0
#         while skip + nth <= len_w:
#             if wildcard_exhaustive(pattern[nth+1:], word[skip+nth:]):
#                     dp[nth+1][skip+nth]
#                     return True
#             skip += 1
#
#     # 다섯 번째 조건
#     return False
#
#
# answer = []
#
# for _ in range(N) :
#
#     wild_card = sys.stdin.readline().rstrip()
#     n = int(sys.stdin.readline().rstrip())
#     strings = []
#
#     for _ in range(n) :
#         strings.append(sys.stdin.readline().rstrip())
#
#     ans = []
#     for string in strings :
#         len_wild = len(wild_card)
#         len_str = len(string)
#         dp = [[None for _ in range(110)] for _ in range(110)]
#         if match(0,0) :
#             ans.append(string)
#             print("ZZ")
#         # if wildcard_exhaustive(wild_card, string) :
#             # print("AA")
#             # ans.append(string)
#
#     answer.extend(sorted(ans))
#
# # answer = sorted(answer)
# for str in answer :
#     print(str)
#
#
#
#
# # 3
# # he?p
# # 3
# # help
# # heap
# # helpp
# # *p*
# # 3
# # help
# # papa
# # hello
# # *bb*
# # 1
# # babbbc
#
#
#
#
#
# # 문제를 어렵게 만드는 부분은 *이다.
# # *에 해당하는 글자가 몇글자인지 마주한 순간에는 알 수가 없다.
# # 그렇기에 앞의 문자열이 잘 매치되다가 *가 나온 순간 wild_card의 *다음에 나오는 문자열과
# # string의 현재 인덱스에서부터 만들 수 있는 모든 문자열과 매칭 함수를 돌려 완전탐색하면 된다.
# # 예를 들어 wild card : "tr*qw" 이고, string : "trqqeettqw" 라면
# # *를 마주한 순간 string의 인덱스는 2로 q일 것이다. 이때 *가 몇개의 문자열에 해당하는지 모르니까 다 만들어 본다
# # qqeettqw, qeettqw, eettqw, ettqw, ttqw, tqw, qw, w
#
#
# # 틀린 이유
# # 재귀 함수를 어떻게 짜야하는지 감이 오질 않았다.
# # 문자열을 하나하나 비교해가면서 한번에 끝내려는 방법을 구상하다가
# # wild card : "t*qw*t" , string : "tqw11111qwt" 와 같은 문자열이 나오면
# # qw에 매칭되는 위치가 앞의 qw인지 뒤의 qw인지 판단할 수 없을 것이라고 생각하고 포기했다.
#
#
# # 중복으로 발생되는 영역이 없어서 memoization이 사용 안될 것 같은데 어디서 쓰는거지?
#
#



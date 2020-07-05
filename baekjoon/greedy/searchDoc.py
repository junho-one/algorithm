import sys

Doc = sys.stdin.readline().rstrip()
String = sys.stdin.readline().rstrip()


cnt = 0
len_str = len(String)

while Doc :
    idx = Doc.find(String)
    if idx != -1 :
        cnt += 1
        Doc = Doc[idx+len_str:]
    else :
        break
print(cnt)

# 설명 x


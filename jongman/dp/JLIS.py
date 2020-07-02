# 왜 시간초과가 뜰까?

import sys

# 1개
T = int(sys.stdin.readline().rstrip())

def JLIS(idx_a, idx_b) :

    if dp[idx_a][idx_b] :
        return dp[idx_a][idx_b]

    now_A = A[idx_a]
    now_B = B[idx_b]

    max_elem = max(now_A,now_B)

    ret = 2
    # ret =2 하는 이유가 맨 처음 수인 A[start_A], B[start_B] 가 들어간다고 생각하고 시작하니까
    # 그 이후로 두 숫자보다 큰 숫자들만 뒤에 쌓이는 것
    # 그리고 맨 마지막을 생각해봐도 (a,b) 뒤에 쌓이는게 없다? 그러면 return 값은 최소 현재 두 인덱스에 해당하는 값 2개

    for i in range(idx_a+1, len_A) :
        if A[i] > max_elem :
            ret = max(ret,JLIS(i,idx_b)+1)

    for i in range(idx_b+1, len_B) :
        if B[i] > max_elem :
            ret = max(ret,JLIS(idx_a,i)+1)

    dp[idx_a][idx_b] = ret
    return dp[idx_a][idx_b]

for _ in range(T) :

    len_A, len_B = map(int, sys.stdin.readline().rstrip().split(" "))

    A = list(map(int,sys.stdin.readline().rstrip().split()))
    B = list(map(int,sys.stdin.readline().rstrip().split()))
    A.insert(0, -sys.maxsize+1)
    B.insert(0, -sys.maxsize+1)
    len_A += 1
    len_B += 1
    dp = [ [ None for _ in range(len_B)] for _ in range(len_A)]

    # [-9223372036854775806, 1, 2, 3]
    # [-9223372036854775806, 4, 5, 6]
    # A와 B 앞에 최소값이 들어가야 한다. 왜냐하면 JLIS는 첫 입력받은 두 인덱스에 해당하는 숫자를 포함하고
    # 그 포함한 문자열 두개를 기반으로 만들 수 있는 가장 큰 길이를 만든다.
    # LIS처럼 한 문자열에서는 for문을 돌려 첫 시작 문장에서 모두 LIS를 돌릴 수 있었지만
    # JLIS에서는 A에서 두 숫자가 먼저 시작 할 수도 있다. 그렇다면 시작할 때 b_idx를 넣어줘야 하는데 방법이 없다
    # 그렇기에 첫 숫자를 가장 작은 수로 지정해놓고 시작하면 저 두 숫자를 포함한 리스트를 시작으로 원본 문자열 두개에서 최장 길이 문장을 찾아낸다.
    # 최소값 두개가 포함되어 있기에 결과에서 2를 뺴주면 된다.

    print(JLIS(0,0)-2)
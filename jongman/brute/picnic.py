N = int(input())

def isDuplicate(pairs) :

    pair_list = sum(pairs, [])
    pair_set = set(pair_list)

    if len(pair_list) != len(pair_set) :
        return True

    else :
        return False


def makePair(count, pair_list, max_pair, max_num) :
    global AA

    if isDuplicate(pair_list) :
        return False

    if len(pair_list) ==  max_pair :
        AA += 1
        return True

    if count >= max_num :
        return False


    makePair(count + 1, pair_list, max_pair, max_num)
    pair_list.append(pairs[count])
    makePair(count + 1, pair_list, max_pair, max_num)
    pair_list.pop()

def pairing( finished ) :

    if all(finished) :
        return 1

    first_people = finished.index(False)
    count = 0

    for i in range(first_people+1, len(finished)) :

        if not finished[i] and areFriend[first_people][i] :

            finished[i] = True
            finished[first_people] = True
            count += pairing(finished)
            finished[i] = False
            finished[first_people] = False

    return count


for _ in range(N) :

    n,m = map(int, input().split())
    pairs = []
    line = list(map(int,input().split()))

    for i in range(0,m*2,2) :
        pairs.append(line[i:i+2])

    # AA = 0
    # makePair(0,[],int(n/2), m)
    # print(AA)



    areFriend = [ [ False for _ in range(n)] for _ in range(n) ]

    for pair in pairs :
        areFriend[pair[0]][pair[1]] = True
        areFriend[pair[1]][pair[0]] = True

    finished = [False for _ in range(n)]

    print(pairing(finished))



# 짝을 만드는 경우의 수를 세는 문제이다. 학생의 수가 10 이하이기 떄문에 완전 탐색으로도 해결 가능하다.
# 처음에는 친구를 의미하는 리스트를 이용하여 완전탐색을 하려고 했지만 최대값이 45로 시간초과가 난다.

# 문제를 자세히 살펴보면 n명의 짝을 짓는 문제이다. 이 문제는 n-2명의 짝을 짓는 문제인 subproblem으로 쪼개질 수 있다.

# (1,4) (3,2) 와 (3,2) (1,4)가 중복되어 나오는 것을 막기 위해서 순서를 강제할 필요가 있다.
# 여기서는 작은 수를 먼저 짝을 맺는 방식을 사용해 중복을 없앴다.



def solution(name) :
    answer = 0

    name = list(name)

    notA = 0
    notA_idxs = []

    for i,n in enumerate(name[1:]) :
        if n != 'A' :
            notA +=1
            notA_idxs.append(i+1)

    idx = 0
    step = 0
    alphToStep = {'A': 0, 'B': 1, 'Z': 1, 'C': 2, 'Y': 2, 'D': 3, 'X': 3, 'E': 4, 'W': 4, 'F': 5, 'V': 5, 'G': 6,
                  'U': 6, 'H': 7, 'T': 7, 'I': 8, 'S': 8, 'J': 9, 'R': 9, 'K': 10, 'Q': 10, 'L': 11, 'P': 11, 'M': 12,
                  'O': 12, 'N': 13}

    # 인덱스 0의 문자는 초기에 넣어줌.
    step += alphToStep[name[0]]
    name[0] = 'A'

    while notA > 0 :
        right = 0
        left = 0

        # 현재 인덱스에서 왼쪽, 오른쪽으로 출발해서 현재 인덱스까지 한바퀴의 문자열들을 담은 배열을 각각 생성
        right_sequence = name[idx + 1:] + name[:idx]
        left_sequence = list(reversed(name[idx + 1:] + name[:idx]))

        # 현재 인덱스에서 오른쪽으로 출발해서 한바퀴
        for ch in right_sequence :
            right += 1

            if ch != 'A' :
                break

        # 현재 인덱스에서 왼쪽으로 출발해서 한바퀴
        for ch in left_sequence:
            left += 1

            if ch != 'A':
                break

        # 왼쪽과 오른쪽으로 갔을 때 가야하는 스텝수가 적은 곳으로 간다.
        if left >= right :
            idx = idx + right
            step += right

        else :
            idx = idx - left
            step += left

        notA -= 1

        # 도착한 곳에서 현재 문자 A를 해당 문자로 바꿔줌.
        step += alphToStep[name[idx]]
        name[idx] = 'A'


    return step
print(solution("JAN"))
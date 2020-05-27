def solution(heights):
    answer = []

    N = len(heights)
    answer = [0 for i in range(N)]
    heights = list(enumerate(heights,start=1))

    prevTop = []

    # heights 배열을 뒤에서부터 탐색
    for idx, top in reversed(heights) :

        if prevTop :
            # prevTop에 값들이 있다면 현재 top의 높이와 비교해서 작다면 빼내고 그 건물 인덱스에 해당하는 자리에 현재 탑의 인덱스 넣기
            for i in range(len(prevTop)-1,-1,-1):
                if prevTop[i][1] < top :
                    answer[ prevTop[i][0]-1 ] = idx
                    del prevTop[i]

        # 과정이 끝나면 무조건 현재 탑을 prevTop에 추가
       prevTop.append((idx,top))

    return answer


solution([6,9,5,7,4])
solution([3,9,9,3,5,7,2])
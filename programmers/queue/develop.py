def solution(progresses, speeds):
    answer = []

    while progresses:

        # 계속해서 speeds만큼 progresses에 더해줌
        progresses = [x + y for x, y in zip(progresses, speeds)]

        if progresses[0] >= 100 :
            count = 0
            i = 0
            # 전체 progresses를 앞에서부터 돌면서 100보다 크거나 같으면 삭제한 뒤 count를 셈
            while i < (len(progresses)) :

                if progresses[i] >= 100 :
                    del progresses[i]
                    del speeds[i]
                    count += 1

                # 100이 아닌 값이 나온 순간 멈춤
                else :
                    break

            answer.append(count)

    return answer

# 100 130 64 150 이면 첫번째 배포에서는 2개만 나와야하는 것
print(solution([93,30,55], [1,30,5]))
print(solution( [ 93 , 30 , 55 , 60 ],[ 1, 30 , 5 , 40 ]))
def solution(arrangement):
    answer = 0

    left = []
    prev = ""
    for bracket in arrangement:

        if bracket == '(' :
            left.append(bracket)

        else :
            # )가 나오면 (와 짝이 나온 것이기 때문에 무조건 pop을 해준다.
            # 여기서 prev가 ( 면 레이저란 의미고, ( 이면 막대기라는 의미다.
            left.pop()
            # 레이저가 나오면 현재 앞에 쌓여있는 막대기 수 만큼 막대기가 생기므로 + len(left)
            if prev == "(" :
                answer += len(left)
            # 막대기가 나오면 그 막대기는 이제 끝임으로 +1을 해준다.
            else :
                answer += 1

        prev = bracket


    return answer

print(solution("()(((()())(())()))(())"))




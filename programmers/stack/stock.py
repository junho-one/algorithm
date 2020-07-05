def solution(prices):
    stack = [(0, prices[0])]
    answer = [0 for _ in prices]
    maxIdx = len(prices) - 1

    # 처음 원소부터 돌면서 stack에 넣는다. 이때 stack top의 price보다 현재 price가 더 작다면
    # while 문을 돌며 stack의 원소들과 비교한다. 현재 price보다 큰 원소들은 모두 pop한 뒤
    # 현재 인덱스와 그 원소의 인덱스의 차이를 answer에 써준다.
    for idx, price in enumerate(prices[1:],start=1):

        top = stack[-1]

        if top[1] > price:
            while stack:         # 스택에는 계속 price의 오름차순으로 값이 쌓여 있다.
                top = stack[-1]

                if top[1] > price:
                    answer[top[0]] = idx - top[0]
                    stack.pop()

                else:
                    break

        stack.append((idx, price))

    # 만약 남아있다면 끝까지 가격이 떨어지지 않은 것을 의미하므로 maxIdx의 차이를 넣어준다.
    if stack :
        for elem in stack :
            answer[elem[0]] = maxIdx - elem[0]

    return answer

print(solution([1, 2, 3, 2, 3]))
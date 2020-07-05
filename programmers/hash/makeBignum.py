def solution(number, k):
    number = list(number)
    number = list(map(int, number))
    stack = [number[0]]

    # 맨 앞자리 부터 차례대로 수를 읽으면서 현재 수가 스택에 있는 값보다 작으면 그냥 넣고
    # 크다면 스택 안에 있으면서 현재 수 보다 작은 수는 다 뺀다.
    # 이 때 스택에서 수를 뺄 때마다 k를 감소시켜 k가 0이 되면 더이상 빼낼 수 없도록 한다.

    for num in number[1:]:

        top = stack[-1]

        # 스택 값과 비교하여 빼내기 k도 같이 비교
        if top < num and k > 0:
            stack.pop(-1)
            k -= 1

            while stack and k > 0:
                top = stack[-1]

                if top < num:
                    stack.pop(-1)
                    k -= 1
                else:
                    break

            stack.append(num)

        # 현재 값이 더 작거나 같으면 그냥 넣음
        else:  # top >= num
            stack.append(num)

    # 만약 k가 0이 아니라면 제거해야함. 뒤를 짜름
    if k > 0 :
        stack = stack[:-k]

    answer = "".join(map(str, stack))

    return answer

print( solution("4177252881",1) )
print( solution("777777",2) )



# 문자열로 계속 비교하면 시간초과
# def solution(number, k):
#     answer = ""
#
#     f_idx = 0
#
#     # print(number)
#     k = k + 1
#
#     while k <= len(number):
#         nowNum = number[f_idx:k]
#         maxNum = max(nowNum)
#         maxIdx = nowNum.index(maxNum)
#
#         answer += nowNum[maxIdx]
#         f_idx = maxIdx+1+f_idx
#         k += 1
#
#     return answer
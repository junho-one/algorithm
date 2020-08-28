# 프로그래머스 N으로 표현
# 못풀었었음. operator 일때는 뒤로 operand, operand 일때는 뒤로 operator 이렇게 재귀로 짜는 방식을 고안했다가 너무 복잡해서 포기
def solution(N, number):

    nums = [set() for _ in range(9)]

    for i in range(8) :
        nums[i+1].add(int(str(N)*(i+1)))
        if number in nums[i+1] :
            return i+1

    # 최대 8이니 1+1, 1+2, 2+2 ... 합이 8이 될 떄 까지 모든 경우를 다 해본다. 그리고
    # i보다는 i+j는 항상 크니 i가 1증가할 때면 i는 더이상 바뀌지 않는다 그렇기에 i를 체크를 해주면 답을 더 빨리 찾을 수 있다.
    for i in range(1, 9) :
        for j in range(1, i+1) :
            for operand1 in nums[i] :
                if i+j <= 8 :
                    # +,-,*은 operand의 위치와 상관없이 값이 같으니 //만 두 경우 다 넣어줌
                    for operand2 in nums[j] :
                        nums[i+j].add( operand1 + operand2)
                        nums[i+j].add( operand1 - operand2)
                        nums[i+j].add( operand1 * operand2)
                        if operand2 != 0 :
                            nums[i+j].add( operand1 // operand2)
                        if operand1 != 0 :
                            nums[i+j].add (operand2 // operand1)
        # if number in nums[i] :
        #     return i

    for idx,num in enumerate(nums) :
        if number in num :
            return idx

    return -1

print(solution(5,12))
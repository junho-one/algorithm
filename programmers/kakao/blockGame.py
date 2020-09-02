from collections import deque

def solution(board):

    def canFall(row, col) :
        for i in range(0, row) :
            if board[i][col] != 0 :
                return False

        return True

    def check_vertical_Rect(row,col) :
        numbers = set()
        zero = 0
        blocks = []
        for i in range(2) :
            for j in range(3) :
                if row+i >= N or col+j >= N :
                    return False

                if board[row+i][col+j] != 0 :
                    # num이 0이 아닌데 현재 값과 다르다면 2개의 값이 있는 것

                    blocks.append((row+i,col+j))

                else :
                    zero += 1
                    if not canFall(row+i,col+j) :
                        return False

                numbers.add(board[row + i][col + j])

        if zero == 2 and len(numbers) == 2:
            return blocks
        else :
            return False

    def check_horizontal_Rect(row, col):
        numbers = set()
        zero = 0
        blocks = []
        for i in range(3) :
            for j in range(2) :
                if row+i >= N or col+j >= N :
                    return False

                if board[row + i][col + j] != 0:
                    # num이 0이 아닌데 현재 값과 다르다면 2개의 값이 있는 것
                    blocks.append((row+i,col+j))


                else:
                    zero += 1
                    if not canFall(row + i, col + j):
                        return False

                numbers.add(board[row+i][col+j])

        if zero == 2 and len(numbers) == 2:
            return blocks
        else :
            return False

    N = len(board)

    answer = 0
    prev_answer = 0

    for _ in range(200) :

        for i in range(N) :
            for j in range(N) :
                blocks = check_horizontal_Rect(i,j)

                if blocks :
                    answer += 1
                    for row,col in blocks :
                        board[row][col] = 0

                blocks = check_vertical_Rect(i,j)

                if blocks :
                    answer += 1
                    for row,col in blocks :
                        board[row][col] = 0

        if prev_answer == answer :
            break

        prev_answer = answer

    return answer


print(solution([[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,6,6,0],
                [0,0,0,0,0,0,4,6,7,0],
                [0,0,0,0,0,4,4,6,7,0],
                [0,0,0,0,3,0,4,0,7,7],
                [0,0,0,2,3,0,0,0,5,5],
                [1,2,2,2,3,3,0,0,0,5],
                [1,1,1,0,0,0,0,0,0,5]]))


# 전체 board에 각 원소를 접근하면서 가로 직사강형, 세로 직사각형을 만들어본다.
# 이때 위에서 2개의 검을 블록이 떨어져서 직사각형이 완성될 수 있고, 그 직사각형을 이루는 blocknumber가 1개일 때 그 block은 지울 수 있게 된다.
# 이를 최대 200번, 블록 개수만큼 반복하면서 더 이상 변화가 없을 때 까지 수행해주면 된다.

# 50*50*6 [직사각형 판별] * 2 를 최대 200번 반복하느 는것
# 최대 600만번의 연산으로 시간안에 문제가 해결 가능하다.


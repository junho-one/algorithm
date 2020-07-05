class Node:
    num = None
    child = None

    def __init__(self, num):
        self.num = num
        self.child = {}


class trie:
    root = None

    def __init__(self):
        self.root = Node("*")

    def add(self, num):

        cur = self.root

        for i in range(len(num)) :
            if cur.child.get(num[i]) == None :
                cur.child[num[i]] = Node(num[i])

            # 값을 넣다가 True를 발견하면 이 위치에서 끝난 문자열이 있으므로 접두사가 존재
            if cur.child.get("True") :
                return True

            cur = cur.child[num[i]]

        # 단어가 들어와서 모두 삽입 했는데 무언가 있다면 현재 단어가 접두사가 됨
        if cur.child :
            return True

        # 핸드폰 번호가 끝나면 True를 넣어 끝난 곳임을 표시
        cur.child['True'] = "*"

        return False

def solution(phone_book):
    answer = True

    tri = trie()

    for num in phone_book :
        if tri.add(num) :
            return False

    return True

# 오답이 나는 부분을 못 찾겠음

import sys

class Node :
    def __init__(self, char, recommend,rec_times, child):
        self.char = None
        self.recommend = "{"
        self.rec_times = rec_times
        self.child = {}

    def get(self, char):
        return self.child.get(char)

    def add(self, char, word, times):
        self.child[char] = Node(char, word,times, {})

    def changeRec(self, word, times):
        if times > self.rec_times \
                or (times == self.rec_times and word < self.recommend):

            self.rec_times = times
            self.recommend = word

    def children(self, char):
        return self.child[char]

    def isRecommend(self, word):
        return self.recommend == word

class Trie :
    def __init__(self):
        self.root = Node(None,None,111,{})

    def add(self, word, times):
        cursor = self.root
        for s in word :

            if not cursor.get(s) :
                cursor.add(s, word, int(times))

            cursor.changeRec(word, int(times))


            cursor = cursor.children(s)
        # cursor.changeRec(word, int(times))

    def find(self, word):
        cursor = self.root
        cnt = -1
        # print("--------------", word)
        for s in word :
            # print(cursor.child,"\n",cursor.recommend,"\n", cursor.char, cursor.rec_times)
            cnt += 1
            if not cursor.get(s) :
                return len(word)

            else :
                if cursor.isRecommend(word) :
                    return min(cnt + 1, len(word))

            cursor = cursor.children(s)

        return len(word)


T = int(sys.stdin.readline().rstrip())

for _ in range(T) :

    N, M = map(int, sys.stdin.readline().rstrip().split(" "))
    trie = Trie()

    for _ in range(N) :
        string, times = sys.stdin.readline().rstrip().split(" ")
        trie.add(string, times)


    typed = sys.stdin.readline().rstrip().split(" ")
    answer = len(typed)-1
    # print(trie.find("ALL"))
    # print(typed)
    for word in typed :
        # print(word, trie.find(word))
        # answer += trie.find(word)
        times = trie.find(word)
        # print(times)
        answer += times

    print(answer)


# 매번 글자를 넣어주면서 트리의 거쳐가는 노드에서 Recommend를 갱신해준다.
# 만약 새로 들어온 문자의 횟수가 기존에 있는 추천단어의 횟수보다 많다면 바꿔주게 된다.

# 찾는 연산에서는 만약 현재 노드의 recommed가 해당 단어라면 +을 해서 반환한다.
# 만약 노드에 자식에 해당 단어의 문자가 없다면 전체 문자열의 길이를 반환하고
# 문자열 끝까지 가서도 recommend와 매칭이 안된다면 문자열의 길이를 반환한다.

# root에도 항상 recommend가 갱신되는데,


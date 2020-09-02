class Trie():

    def __init__(self) :
        self.root = Node("ROOT")

    def add(self, string):
        pf = self.root
        for s in string :
            if not pf.exists(s) :
                pf.makeChild(s)

            pf.childPlus()
            pf = pf.getChild(s)

        pf.makeChild("END")
        pf.childPlus()

    def get(self, string):
        pf = self.root
        cnt = 0
        for s in string :
            pf = pf.getChild(s)
            cnt += 1
            # print(pf.char, pf.child, cnt, pf.childNum)
            if pf.childNum <= 1 :
                return cnt

        return cnt

class Node():

    def __init__(self, char):
        self.char = char
        self.childNum = 0
        self.child = {}

    def exists(self, s):
        return self.child.get(s)

    def getChild(self, s):
        return self.child[s]

    def makeChild(self, s):
        self.child[s] = Node(s)

    def childPlus(self):
        self.childNum +=1

def solution(words):
    print(words)
    trie = Trie()

    for word in words :
        trie.add(word)

    answer = 0
    for word in words :
        answer += trie.get(word)


    return answer

# print(solution(['abc','def','ghi','jklm','adbc','abedef']))
print(solution(['abc','def','ghi','jklm']))
print(solution(['go','gone','guild']))
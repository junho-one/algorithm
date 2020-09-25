import sys

N = int(sys.stdin.readline().rstrip())

words = []
wordset = set()
for i in range(N) :
    words.append(sys.stdin.readline().rstrip())
    wordset = wordset | set(list(words[i]))

print(wordset)
print(words)

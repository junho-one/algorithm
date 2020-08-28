# 프로그래머스 가장 긴 팰린드롬

# 효율성 실패
def pelindrome(str) :

    end = len(str) - 1
    start = 0

    while start < end :
        if str[start] != str[end] :
            return 0
        start +=1
        end -= 1

    return len(str)

def solution(s):
    answer = 0
    s = list(s)
    for lo in range(len(s)) :
        for hi in range(len(s), lo, -1) :
            if answer <= hi-lo :
                answer = max(answer, pelindrome(s[lo:hi]))

    return(answer)

# 성공
def solution(s) :

    def pelindrome(start,end) :
        if end >= len(s) or s[start] != s[end] :
            return 0

        while start-1 >= 0 and end+1 < len(s) and s[start-1] == s[end+1] :
            start -= 1
            end += 1

        return end-start+1

    answer = 0
    for i in range(len(s)) :
        answer = max(answer, pelindrome(i,i), pelindrome(i,i+1))

    return answer

print(solution("abcdcba"))
print(solution("abacde"))
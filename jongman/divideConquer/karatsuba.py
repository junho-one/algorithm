# 풀어봐야 함

a = [1,2,3,4,5,6]
b = [7,6,5,4,3]

def multiply(A,B) :

    if not A :
        return B
    if not B :
        return A

    result = [0 for _ in range(len(A) + len(B))]

    # 기본 곱셈
    for b_i, b in enumerate(B) :
        for a_i, a in enumerate(A) :
            result[b_i+a_i] += b*a

    return normalize(result)

def normalize(number) :
    number.append(0)

    for i in range(0, len(number)-1) :
        if number[i] < 0 :
            burrow = ( abs(number[i]) + 9) // 10
            number[i+1] -= burrow
            number[i] += burrow * 10

        else :
            number[i+1] += number[i] // 10
            number[i] %= 10

    while number and number[-1] == 0:
        number.pop()

    return number

def addTo(A,B) :

    maxLen = max( len(A), len(B))

    i = 0
    result = [ 0 for _ in range(maxLen+1)]
    while i < maxLen :
        sum_i = 0
        if i >= len(A) :
            sum_i = B[i]
        elif i >= len(B) :
            sum_i = A[i]
        else :
            sum_i = A[i] + B[i]

        result[i] = sum_i
        i+=1
    return normalize(result)

def shift(number, n) :
    return [0] * n + number

def subFrom(A,B) :

    maxLen = len(A)

    i = 0
    result = [ 0 for _ in range(maxLen)]
    while i < maxLen :
        sum_i = 0
        if i >= len(B) :
            sum_i = A[i]
        else :
            sum_i = A[i] - B[i]

        result[i] = sum_i
        i+=1

    return normalize(result)


def karatsuba(a,b) :
    print(a,b)
    len_a = len(a)
    len_b = len(b)

    if len_a < len_b :
        karatsuba(b,a)

    if len_a <= 2 or len_b <= 2 :
        return multiply(a,b)


    mid_a = len_a // 2
    if len_a %2 == 1 :
        mid_a += 1

    mid_b = min(len(b), mid_a)

    up_a = a[:mid_a]
    up_b = b[:mid_b]
    down_a = a[mid_a:]
    down_b = b[mid_b:]

    # a0 * b0
    print("before", down_a, down_b)
    z0 = karatsuba(down_a, down_b)
    print("after", z0)
    # a1 * b1
    z2 = karatsuba(up_a, up_b)
    # (a0+a1) * (b0+b1) - z0 - z2
    # print(addTo(up_a,down_a) , addTo(up_b,down_b), "Q" , up_a,down_a)
    z1 = karatsuba(addTo(up_a,down_a), addTo(up_b,down_b))
    # print("z1",z1)
    z1 = subFrom(z1, z0)
    z1 = subFrom(z1,z2)

    ret = []
    ret = addTo(z0,ret)
    ret = addTo(ret, shift(z1, mid_a))
    ret = addTo(ret, shift(z2, mid_a*2))
    # print("Q",ret)
    return normalize(ret)



print(karatsuba(a,b))

print(subFrom(a,b))
print(subFrom(b,a))
print(addTo(a,b))
print(addTo(b,a))


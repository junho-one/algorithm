# 풀어봐야 함

a = [1,2,3,4,5,6]
b = [7,6,5,4,3,2]


def multiply_bigNum(a,b) :

    len_a = len(a)
    len_b = len(b)

    if len_a == 1 :
        return b
    if len_b == 1 :
        return a

    up_a = a[:len_a // 2]
    up_b = b[:len_b // 2]
    down_a = a[len_a // 2:]
    down_b = b[len_b // 2:]

    z0 = multiply_bigNum(down_a, down_b)
    z2 = multiply_bigNum(up_a, up_b)
    z1 = multiply_bigNum(add(up_a, down_a),  add(down_a, down_b) ) -z0 -z2









import itertools

def isPrime(n) :

    for i in range(2,n) :
        if n % i == 0 :
            return False

    return True

def solution(numbers):
    answer = 0

    number_list = list(numbers)

    allcase = []

    for i in range(1,len(number_list)+1) :

        allcase.extend(list(itertools.permutations(number_list , i)) )

    allcase = list( map( lambda x : x if x[0] != '0' else None, allcase) )
    primes = set()
    for num in allcase :
        if num:
            num = int("".join(num))

            if num == 1 :
                continue

            if num not in primes and isPrime(num) :
                primes.add(num)

    return len(primes)


solution("11307")
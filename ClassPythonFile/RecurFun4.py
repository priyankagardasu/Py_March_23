import sys

# print(sys.getrecursionlimit())

sys.setrecursionlimit(10**9)


def factorialNum(num):
    if num == 1:
        return num
    return num * factorialNum(num-1)

def sumOfN(n):
    if n == 1:
        return n
    return n + sumOfN( n- 1)

# print(factorialNum(999))
print(sumOfN(10000))


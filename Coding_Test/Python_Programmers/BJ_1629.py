def calc(A, B, C):

    result = A**B%C

    return result

A, B, C = map(int, input().split())

print(calc(A, B, C))


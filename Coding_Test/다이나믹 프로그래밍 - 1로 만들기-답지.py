x = int(input("정수를 하나 입력하세요: "))

d= [0]*(x+1)

for i in range(2, x+1):
    d[i] = d[i-1] + 1

    if i % 2 ==0:
        d[i] = min(d[i], d[i//2]+1)

    if i % 3 ==0:
        d[i] = min(d[i], d[i//3]+1)

    if i % 5 ==0:
        d[i] = min(d[i], d[i//5]+1)

    print(d)

print(d[x])


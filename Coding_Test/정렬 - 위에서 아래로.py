N = int(input('500 이하의 정수 한개 입력: '))

list1=[]

for n in range(N):
    M = int(input("{0}개 중 {1}번째 정수 입력:".format(N, n+1)))
    list1.append(M)

list1.sort(reverse=True)

print()

for p in list1:
    print(p, end=" ")

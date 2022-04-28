import heapq as hq
N = int(input('500 이하의 정수 한개 입력: '))

heap0=[]

for n in range(N):
    M = int(input("{0}개 중 {1}번째 정수 입력:".format(N, n+1)))
    hq.heappush(heap0, M)

print()

for p in reversed(heap0):
    print(p, end=" ")

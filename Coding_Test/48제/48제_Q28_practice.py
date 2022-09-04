"""
이진 탐색 문제

문제 풀이에서는 재귀함수로 풀었던데 나는 범위만 나눠서 내 방식대로 풀어봤음.
"""
#L=input(list(input("정수 입력 : ")))
L=[-15, -4, 2, 8, 9, 13, 15]
answer=-1

start=0
end=len(L)-1
mid=(start+end)//2

#print(start, mid, end)
#print(L[mid], mid)

if L[mid]==mid:
    print(mid)
    
elif L[mid]>mid:
    print("전방 탐색")
    for n in range(start, mid):
        if n==L[n]:
            print(n)
            break
else:
    print("후방 탐색")
    for n in range(mid, end):
        if n==L[n]:
            print(n)
            break

# 2. 숫자 카드 게임 (그리디)

M,N = map(int, input('행과 열의 숫자를 스페이스로 구분하여 입력 : ').split())

list2=[]
for n in range(N):
    list1 = list(map(int, input(str(M)+'개의 숫자를 스페이스로 구분하여 입력').split()))
    min1 = min(list1)
    list2.append(min1)
final_min=min(list2)

print('\nAnswer >>', final_min)

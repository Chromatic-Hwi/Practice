# 2. 1이 될때까지 (그리디)

N, K = map(int, input('두 개 숫자를 스페이스로 구분하여 입력 : ').split())

Count = 0

while (N>=K):
    while (N%K!=0):
        N-=1
        Count+=1
    N//=K
    Count+=1
    
# 나눔+빼기의 일련 과정 처리 후 마지막 남은 수에 대해 1씩 뺴기 최종 정리 과정
while (N>1):
    N-=1
    Count+=1
        
print('Answer >>', Count)

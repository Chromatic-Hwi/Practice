# 2. 큰수의 법칙 (그리디)

"""
n = 연산에 쓰일 숫자 갯수
m = 전체 반복 가능 횟수
k = 제일 큰 수가 반복될 수 있는 횟수
"""

n,m,k = map(int, input('type 3 number with space : ').split())
data = list(map(int, input('type '+str(n)+' number withe space : ').split()))
data.sort()
print('\nSorted Data >>',data)
first = data[-1]
second = data[-2]

"""
서로 다른 배열 위치의 숫자는 다른 수로 취급하여 그대로 덧셈을 진행하는데 만약 1번째와 2번째가 값이
같더라도 서로 다른 변수로 저장되어 계산되므로 더 이상의 코드는 필요없음.
"""

result=0
T=0
while (True):
    if(m==0):
        break
        
    print('\n<This is Seq',str(T+1)+'>')
    
    for p in range(k):
        print('biggest number added')
        result+=first
        m-=1
        print(result)
    result+=second
    m-=1
    print('second biggest number added')
    print(result)
    
    T+=1

print('\n<Result> >> ',result)

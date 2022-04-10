# 2. 1이 될때까지 (그리디)

N, K = map(int, input('두 개 숫자를 스페이스로 구분하여 입력 : ').split())

Numb = N
Count = 0

while True:
    remainder=Numb%K
    if (remainder==0):
        while True:
            Numb/=K
            Count+=1
            if (remainder!=0 or int(Numb)==1):
                break
    elif(remainder!=0 and int(Numb)!=1):
        Numb-=1
        Count+=1
    
    else:
        break
        
print('Answer >>', Count)

"""
N과 K가 25, 5일때의 상황을 출력 결과를 보면서 제작했기 때문에 25와 5가 아닌
다른 숫자를 입력하면 제대로 작동하지 않는 에러 발생.

하나의 경우에만 고착하지 않도록 생각을 잘 해야함.
"""

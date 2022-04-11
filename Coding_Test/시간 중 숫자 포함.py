# 시간 중 특정 숫자 포함 (구현)

H = int(input('0~23의 숫자 중 하나 입력 :'))

Count=0

for h in range(H+1):
    for m in range(60):
        for s in range(60):
            if('3' in str(h)+str(m)+str(s)):
                Count+=1

print(Count)
    

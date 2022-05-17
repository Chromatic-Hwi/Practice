N=int(input("점수를 입력하세요 : "))

S=str(N)

neck=0
leer=0

for i in range(len(S)):
    if i<len(S)/2:
        neck+=int(S[i])
    if i>=len(S)/2:
        leer+=int(S[i])

if neck==leer:
    print("LUCKY")
else:
    print("READY")
    

"""
답안 예시에는 for문을 두개로 나눠서 전체 문자열의 앞과 뒤를 따로 반복했는데

나는 for문 하나에서 if로 경우를 나눴음. 결국 반복이 도는 시간은 동일하겠지만 for문을 최소화하고자 해당 구조로 썼음.

그외 작동 원리는 같음. 
"""

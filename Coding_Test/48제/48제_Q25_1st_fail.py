# 실패율 = 스테이지 도달 but 클리어 못함 / 스테이지 도달 플레이어 수

# 스테이지 개수 N, 멈춘 스테이지 번호 배열 stages 주어짐.

N = int(input("스테이지의 층수를 입력하세요 : "))

stages = list(map(int, input("멈춘 스테이지의 층을 입력하세요 :").split()))
stages.sort()

length=len(stages)

answer=[]

for n in range(1, N+1):
    
    count=stages.count(n)

    if length==0:
        fail=0
    else:
        fail = count/length

    answer.append((n, fail))
    length-=count

print(answer)

answer = sorted(answer, key=lambda x: x[1], reverse=True)

print(answer)

answer_final = [i[0] for i in answer]

print(answer_final)
    

"""
다음 층으로 넘어갈 때마다 stages에서 빼는건 생각을 했는데 리스트내 카운트법을 몰랐고(일치 조건으로만 검색하려 했음.)

문제 이해를 잘 못했었음.

예시 답안을 확인했더니 핵심 반복문 밖으로 길이 변수를 빼서 계산 관리를 해줘야 하고,
실패율은 별도 계산, 결과를 담은 answer 리스트에는 (층수, 실패율)의 형태로 원소를 담고
sort가 아닌 sorted 처리를 한 최종 답안 출력에서는 각 원소의 0번째 원소인 층수만 출력하도록 해야되기 때문에

느끼기엔 까다로운 처리가 필요한 복잡한 문제로 느꼈음.

"""

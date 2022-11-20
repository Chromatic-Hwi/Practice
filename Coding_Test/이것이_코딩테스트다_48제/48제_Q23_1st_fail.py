N = int(input("학생수를 입력하세요 : "))

score=[]

for _ in range(N):
    score.append(list(input("학생의 이름과 국영수 순으로 점수를 입력하세요 : ").split()))

print(score)

score.sort(key=lambda x:
           (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for score in score:
    print(score[0])
    
"""
첫 시도때는 리스트에 담기만 하고 각 인덱스별 비교는 너무 구조가 복잡해지기 때문에 시도를 하지 않았음.
고민만 하다가 실패.

sort에서 key=lambda x를 이용해서 우선순위에 맞게 정렬하는 법을 기억할 것.

-int(x[1]), int(x[2]) 와 같이 부호로 구분했는데 -는 내림차순, 기본은 오름차순으로 정렬된다.
"""

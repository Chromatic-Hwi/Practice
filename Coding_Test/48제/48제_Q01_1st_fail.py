N = int(input("모험가의 수 N 입력 : "))
print()

adv = []
for i in range(N):
    p = int(input("공포도를 입력하세요: "))
    adv.append(p)

adv.sort()

result=0
group=0

for i in adv:
    group+=1
    if group >= i:
        result+=1
        group=0

print(result)


"""
p.311

문제가 답으로 요구하는 것은 최댓값, 즉 카운트된 상수인데
'그룹으로 만드는 것'이란 사람 사고틀에 갇혀서 리스트나 묶는데만 집중함.

실제 풀이는 오름차순으로 정렬해서 해당 순번의 원소와 갯수를 비교하는 거였음.

전에도 느꼈는데 코드의 요구하는 답이 뭔지를 정확히 이해하고 컴퓨터적인 사고 접근이 필요함.

"""

print("이 게임은 2명 이상 200명 이하 플레이어로 진행됩니다. \n")

N = int(input("플레이어수를 입력하세요? : "))
print()

Total_list=[]
answer=[]

for i in range(N):
    L = list(map(int, input("1 이상 100 이하의 정수를 3개 입력하세요? :  ").split()))
    Total_list.append(L)
    answer.append([0])
    print("*Player_"+str(i+1),"->", L, "\n")

    
#print(Total_list)
#print(answer)

"""
이해를 위한 낙서
[100, 99, 98]
[100, 97, 92]
[63, 89, 63]
[99, 99, 99]
[89, 97, 98]

[100, 100, 63, 99, 89]
[99, 97, 89, 99, 97]
[98, 92, 63, 99, 98]
"""


for i in range(3):
    step_list=[]
    for j in range(N):
        step_list.append(Total_list[j][i])
    #print(step_list)
    for k in range(N):
        if step_list.count(step_list[k])==1:
            answer[k].append(step_list[k])

#print(answer)

for i in range(N):
    print("*Player_"+str(i+1), "Score => ",sum(answer[i]))
    print()
    

    

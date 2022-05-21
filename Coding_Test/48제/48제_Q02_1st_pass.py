S=str(input("각자리가 숫자로 구성된 문자열 입력 : "))

N_list=[]

for i in range(len(S)):
    N_list.append(int(S[i]))

result=1

for i in range(len(N_list)):
    if N_list[i]==0:
        result+=N_list[i]
    else:
        result*=N_list[i]
    
print(result)

"""
자정 넘기기전에 커밋할거라고 서둘렀는데 삽질해버려서 8분 정도 걸린 해결시간 중에 2분은 갖다버림.

0이 등장할경우 문제 설명에서는 괄호로 묶고 더해주고 하는 식으로 처리를 했는데

0에 포커스를 두지않고(0은 사실 결과값에 영향을 못준다고 봐도 될듯) 0 다음 수에 집중하니 금방 풀렸음.

0을 만났을때 결과값 변수 result에는 뭘 해주고 그 다음값을 어떻게 해줄지가 관건이었음.

쉽게 푼 문제였음.
"""

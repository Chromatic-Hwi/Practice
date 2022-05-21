S = list(str(input("0과 1로만 이루어진 문자열을 입력하세요 : ")))

print(S)

answer=[]
answer_s=[]

for i in range(len(S)):
    if i==0:
        answer_s.append(S[i])
    else:
        if answer_s[0]==S[i]:
            answer_s.append(S[i])
        if answer_s[0]!=S[i]:
            answer.append(answer_s)
            answer_s=[S[i]]
        if i==len(S)-1:
            answer.append(answer_s)
            
print(answer)

print(len(answer)//2)



"""
완료 시간은 제한시간 20분 다 채웠거나 살짝 넘긴듯함. (생각해보니 책에는 입력예시가 1개 뿐이라 추가로 더 만들어서 해본다고 더 걸림.)

핵심적인 동작을 떠올린 다음부터는 구현하는데 문제가 되지 않음.

0과 1로만 이루어진 문자열에서 0이 이어지는 구간과 1로 이어지는 구간이 있는데
그걸 for문을 전체 1번 돌면서 작은 리스트엣 담아서 최종 정답 리스트에 담으면 정답리스트 길이를 2로 나눈 몫이 바로 바꾸기 위한 최소 횟수가 됨.

예시 답안과 비교 결과 좀더 직관적인 풀이는 내 풀이인듯 함.

"""

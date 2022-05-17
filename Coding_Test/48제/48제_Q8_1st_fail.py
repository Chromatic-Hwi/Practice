S = str(input("문자열을 입력하세요: "))
S=sorted(S)
print(S)

result=[]
sum_num=0

for i in S:
    if i.isalpha():
        result.append(i)
    else:
        sum_num+= int(i)
result.append(str(sum_num))
result_str="".join(result)

print(result_str)

"""
문자열 내림차순 정렬을 하지 못했음.
예시 답안에는 알파벳 문자열에 바로 sort를 사용했는데 임의의 단어로 테스트 해봐도 안됨.
sorted를 사용하는게 맞다고 봄.

처음 생각에는 리스트로 값들을 받아서 문자열로 결합해서 출력하는게 비효율적일것 같아서
문자열에 더하기로 해봤는데 안되서 결국 리스트로 처리.

문자열을 정렬해서 타입이 문자열이냐, 정수형이냐로 구분했었는데 출력확인해보니 다 문자열로 나왔음.
예시 답안에는 isalpha를 썼던데 공부해보고 외워야겠음.
>> 확인 결과 한글포함 isalpha 사용가능, 숫자는 isdigit()으로 사용!

"""

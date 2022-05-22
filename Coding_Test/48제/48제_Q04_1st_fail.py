import psutil

N = int(input("동전의 갯수를 입력하세요 : "))

coin = list(map(int, input("동전의 금액을 공백으로 구분하여 입력하세요 : ").split()))
coin.sort()

value_list=[]

for i in range(N-1):
    value_list.append(coin[i]+coin[i+1])
    value_list.append(coin[0]+coin[i+1])
for i in range(N-2):
    value_list.append(coin[i]+coin[i+1]+coin[i+2])
    value_list.append(coin[0]+coin[i+1]+coin[i+2])
    
value_list.sort()
print(value_list)

print()
print("Used Memory >>", int(psutil.virtual_memory()[3])//(10**6), "Mb")


"""
반복문을 여러번 거치기엔 주어진 동전의 수에 맞춰진 코드이고 메모리 검사 결과 초과라 실패했음.

예전에 프로그래머스에서 가능한 경우의 수를 조합하는 코드를 봤었는데 기억이 안남.

예시 답안을 봤는데 시작 수 target을 1로 잡았고, 1이 포함되지 않은 많은 수의 금액 조합은 설명이 안 되어있음.
정상 실행이 안될지도 모름.

인터넷 검색도 해봤는데 2개의 동전만 더할 생각을 하지, 전체 경우의 수를 다 고려하진 않음.


"""

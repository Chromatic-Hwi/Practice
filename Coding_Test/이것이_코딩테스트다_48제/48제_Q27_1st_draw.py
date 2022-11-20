import psutil

N=int(input("원소의 개수를 입력하세요 : "))
x=int(input("x의 값을  입력하세요 : "))

list1=list(map(int, input("N개의 정수를 공백으로 구분 입력 하세요 : ").split()))

print(list1)

result=list1.count(x)
if result==0:
    result=-1
print(result)

print()
p=psutil.Process()
rss=p.memory_info().rss/2**20
print(rss, "MB")


"""
1차만에 작동은 시켰는데 문제의 시간 복잡도 조건에는 안 맞음.
이진 탐색으로 풀라고 되어있는데 예시 답안의 1번 보다는 2번의 bisect 모듈을 쓰는게 훨씬 나아보임.

+메모리 계산 정상화했음.
"""

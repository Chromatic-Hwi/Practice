from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    print("\n", l, "\n")
    s = list(map(sum, product(*l)))
    print(s, "\n")
    count = s.count(target)
    print("\n",count)
    return count

numbers = list(map(int, input("2개 이상, 20개 이하의 50 이하 양의 정수를 입력: ").split()))
target = int(input("1000 이하의 타겟 점수를 입력:"))


solution(numbers, target)

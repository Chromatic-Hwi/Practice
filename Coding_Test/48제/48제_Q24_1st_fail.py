N = int(input("집의 수를 입력하세요 : "))

house = list(map(int, input("집의 위치를 공백으로 구분해 입력하세요 : ").split()))

if (N!=len(house)):
    print("집의 수와 위치수가 일치하지 않습니다! \n")

else:
    house.sort()

    result = house[(N-1)//2]

    print(result)

"""
정렬 후 제일 작은 원소와 나머지 연산 후 오른쪽으로 삭제, 재추가?

하나의 원소와 나머지 원소들의 차를 자동으로 계산해주는 툴이 있으면 편하겠는데 모르겠음.

단순 중앙 원소가 답이라는게 허탈함. 나도 생각은 했었는데 예외의 경우를 너무 생각했다가 어렵게 꼬아버리는 꼴이 됨.


"""

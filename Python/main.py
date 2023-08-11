'''
import squareX

print(squareX.base) # 모듈.변수 형식으로 모듈 내부의 변수 사용
print(squareX.square(10)) # 모듈.함수() 형식으로 모듈의 함수 사
'''

from squareX import square

print(square(10))

"""
파이썬에선 for문의 지정 범위 완전 루프 여부와 else를 짝으로 매칭 가능하다.
"""

test_nums = range(2, 121)
answer_nums = []

for num in test_nums:
  num_root = num ** 0.5
  for i in range(2, int(num_root) + 1):
      if num % i == 0:
          break
  else:
      answer_nums.append(num)

print(answer_nums)

price = int(input('금액을 입력하시오'))
count=0

coin_types=[500, 100, 50, 10]

for coin in coin_types:
    count += price // coin
    price %= coin
    
print(count)

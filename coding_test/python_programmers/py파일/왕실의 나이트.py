# 왕실의 나이트 (구현)

X={'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

x,y = map(str, input('현재 나이트가 위치한 좌표를 알파벳, 숫자 순으로 입력: '))


move_types=[[2,1],[1,2],[-2,1],[-1,2],[2,-1],[1,-2],[-2,-1],[-1,-2]]

Count=0

for T in range(len(move_types)):
    print('\n',T+1, '유형')
    nx=X[x]
    ny=int(y)
        
    nx+=move_types[T][0]
    ny+=move_types[T][1]
        

    if (nx>0 and ny>0 and nx<9 and ny<9):
        print(nx, ny)
        Count+=1

    else:
        continue
    
print('Result >>', Count)

# 상하좌우 격자 이동 (구현)

N=int(input('정방 격자의 사이즈를 입력 : '))

N+=1
X=1
Y=1

move_list=list(input('L, R, U, D로 구분된 이동 명령을 입력 :').split())
print(move_list)

for m in range(len(move_list)):
    Direc = move_list[m]
    
    if(Direc == 'L'):
        print('좌로 이동')
        X-=1
        if(X<1):
            X+=1
            
    elif(Direc == 'R'):
        print('우로 이동')
        X+=1
        if(X>N):
            X-=1
            
    elif(Direc == 'D'):
        print('아래로 이동')
        Y+=1
        if(Y>N):
            Y-=1
            
    elif(Direc == 'U'):
        print('위로 이동')
        Y-=1
        if(Y<1):
            Y+=1
            
    else:
        print('Wrong Input!')
        print(Direc)
        
print('Result >>', '('+str(X)+','+str(Y)+')')

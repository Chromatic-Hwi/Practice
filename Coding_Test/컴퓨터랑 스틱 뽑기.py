import numpy as np

stick=12
print('<게임 시작>\n')
while (stick>=1 and stick<13):

    # 사람 차례
    print('당신의 차례입니다.')
    while(stick>1):
        print('남은 스틱의 갯수 >>', stick)
        while(True):
            number=int(input('뽑을 스틱의 수를 골라주세요.(1~3 범위): '))
            if(1<=number and number<=3):
                if(number>=stick):
                    print('※ 고의로 승부에서 지는 행위는 좋은 자세가 아닙니다. 다시 입력하세요')
                else:
                    break
            else:
                print('※ 1~3 사이의 숫자로 입력해주세요.')
            
        stick=stick-number
        print('[당신은 {0}개의 스틱을 뽑았습니다. 남은 스틱 갯수 >> {1}]\n'.format(number, stick))
        break
        
    if(stick==1):
        print('당신이 이겼습니다. :D')
        break
        
    # 컴퓨터 차례
    print('컴퓨터의 차례입니다.')
    while(stick>1):
        print('남은 스틱의 갯수 >>', stick)
        while(True):
            number=np.random.randint(1, 4)
            if(number>=stick):
                pass
            else:
                break
                
        stick=stick-number
        print('[컴퓨터는 {0}개의 스틱을 뽑았습니다. 남은 스틱 갯수 >> {1}]\n'.format(number, stick))
        break
        
    if(stick==1):
        print('당신이 졌습니다. :(')
        break
        
print('<게임 끝>')

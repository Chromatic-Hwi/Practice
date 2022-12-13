import pickle
import os

YN = input("셋업 정보 저장 과정 실행 여부를 입력해주세요. (Y/N)\n>> ")
print()

if YN.upper() == "Y":
    if os.path.isfile('./SetInfo.pkl'):
        print("\n셋업 정보가 새로 생성됩니다. 허용하시면 Y 를 입력해주세요.")
        YN = input("진행 여부 (Y/N)\n>> ")
        if YN.upper() == "Y":
            M_List = list(input("\nM으로 구분된 설비를 입력해주세요. (ex.M1_1 M1_2 M2 M3 대소문자 구분X) \n>> ").split())
            for _ in range(len(M_List)):
                M_List.append(M_List[0].upper())
                del M_List[0]


            TotalLineList = []
            TotalLineCnt = []
            for L in range(len(M_List)):
                print("\n{} 설비에서 Align으로 구분되는 라인을 공백으로 구분해 입력해주세요. (ex. AA CA SV 대소문자 구분X)".format(M_List[L]))
                LineList = list(input(">> ").split())

                for _ in range(len(LineList)):
                    LineList.append(LineList[0].upper())
                    del LineList[0]
                
                TotalLineList.append(LineList)
                TotalLineCnt.append(len(LineList))
                
            TotalCamNumList = []
            for M in range(len(M_List)):
                CamNumList=[]
                for L in TotalLineList[M]:
                    print("\n{} 설비 - {} 라인의 카메라 수를 입력해주세요.".format(M_List[M], L))
                    CamNum = input(">> ")
                    CamNumList.append(CamNum)
                TotalCamNumList.append(CamNumList)
                
            FinalLineList = []
            for x in range(len(TotalLineList)):
                for x2 in TotalLineList[x]:
                    FinalLineList.append(x2)
                    
            '''  
            print(M_List)
            print(TotalLineList)
            print(TotalLineCnt)
            #print(FinalLineList)
            print(TotalCamNumList)
            '''

            TotalLineNCam=[]
            for i in range(len(TotalLineList)):
                LineNCam = dict(zip(TotalLineList[i], TotalCamNumList[i]))
                TotalLineNCam.append(LineNCam)

            #print(TotalLineNCam)

            # 이후 코드 실행에 필요한 인자들은 M, M들의 line별 리스트=TotalLineList의 소리스트,  각 line의 cam 수=TotalLineNCam의 소딕셔너리
            M = len(M_List)

            Result = [M, TotalLineList, TotalLineNCam]

            with open("SetInfo.pkl", 'wb') as f:
                pickle.dump(Result, f)
    else:
        sys.quit()
        
elif YN.upper() == "N":
    with open("SetInfo.pkl", 'rb') as f:
        Info = pickle.load(f)
    print("저장된 셋업 정보\n>> ", Info)



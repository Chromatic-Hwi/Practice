import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import os
import pickle
import time
import scipy.stats as stats
import sys
##############################################################################################################################################
AlphabetList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
##############################################################################################################################################
def HeatMap(Data, Name, Path):
    plt.figure(figsize=(60, 40))
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    sns.heatmap(Data, annot=True, fmt='.3f', annot_kws={"size": 25}, cmap='summer', cbar=False)
    plt.title(Name, pad=50, fontsize=50)
    plt.savefig(Path+"/"+Name+'.png')
    plt.close()
##############################################################################################################################################
def LogSave(Check, ErrorMsg):
    now = time
    startTime = now.strftime('%Y-%m-%d %H:%M:%S')
    #print(startTime)
    path='./'
    LogCheck = os.listdir(path)
    if "Log.txt" not in LogCheck:
        print("\nLog file Created!")
        file = open("./Log.txt", "w")
        file.write("<<Auto DotDist - Run Log>>")
        file.close
    else:
        print("\nLog file Saved.")
        if Check=="work":
            with open('./Log.txt', "a") as file:
                file.write("\n"+startTime)
        else:
            with open('./Log.txt', "a") as file:
                file.write("\n"+startTime+"\t")
                file.write(ErrorMsg)
##############################################################################################################################################
def ValueHandle(InputData):
    data = InputData
    
    columnsLen = len(data.columns)
    NewColumns = AlphabetList[:columnsLen]
    data.columns = NewColumns
    
    DfList=[]
    for col in data.columns:
        columnsList = list(data[col].values.tolist())
        DfList.extend(columnsList)
    DfList_NoNan = [x for x in DfList if np.isnan(x) == False]
    
    data_max = round(np.max(DfList_NoNan), 3)
    data_mid = round(np.median(DfList_NoNan), 3)
    data_min = round(np.min(DfList_NoNan), 3)
    data_gap = round((data_max - data_min), 3)#
    data_avg = round(np.mean(DfList_NoNan), 3)#
    data_var = round(np.var(DfList_NoNan), 3)#
    data_std = round(np.std(DfList_NoNan), 3)#
    return(data_max, data_mid, data_min, data_gap, data_avg, data_var, data_std)
##############################################################################################################################################
def INFO(YN):
    if YN.upper() == "Y":
        M_List = list(input("\nMode로 구분된 설비를 입력해주세요. (ex.M1_1 M1_2 M2 M3 대소문자 구분X) \n>> ").split())
        for _ in range(len(M_List)):
            M_List.append(M_List[0].upper())
            del M_List[0]

        TotalLineList = []
        TotalLineCnt = []
        for L in range(len(M_List)):
            print("\n{} 설비에서 Align으로 구분되는 라인을 공백으로 구분해 입력해주세요. (ex. PA1 PA2 AA CA SV 대소문자 구분X)".format(M_List[L]))
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

        Result = [M_List, TotalLineList, TotalLineNCam]

        with open("SetInfo.pkl", 'wb') as f:
            pickle.dump(Result, f)

        return Result
                
    else:
        print("Exit.")
        sys.exit()
##############################################################################################################################################
YN = input("[셋업 정보 생성] 실행 여부를 입력해주세요. (Y/N)\n>> ")
print()

if YN.upper() == "Y":
    if os.path.isfile('./SetInfo.pkl'):
        print("\n셋업 정보가 새로 생성됩니다. 허용하시면 Y 를 입력해주세요.")
        YN = input("진행 여부 (Y/N)\n>> ")
        LoadInfo = INFO(YN)
    else:
        LoadInfo =INFO(YN)
        
elif YN.upper() == "N":
    try:
        with open("SetInfo.pkl", 'rb') as f:
            LoadInfo = pickle.load(f)
        print("저장된 셋업 정보\n>> ", LoadInfo)
    except FileNotFoundError:
        print("Error!  불러올 셋업 파일이 없습니다!")
        print("\n셋업 정보가 새로 생성됩니다. 허용하시면 Y 를 입력해주세요.")
        YN = input("진행 여부 (Y/N)\n>> ")
        LoadInfo = INFO(YN)

else:
    print("잘못된 입력입니다. 프로그램을 종료합니다.")
    time.sleep(1)
    sys.exit()
##############################################################################################################################################
M_List = LoadInfo[0]
TotalLineList = LoadInfo[1]
TotalLineNCam = LoadInfo[2]
##############################################################################################################################################
try:os.mkdir('./DotDist_Input')
except FileExistsError:pass

for M in range(len(M_List)):
    try:
        os.mkdir('./DotDist_Input/'+str(M_List[M]))
    except FileExistsError:
        pass

    for L in range(len(TotalLineList[M])):
        try:
            Line = TotalLineList[M][L]
            path='./DotDist_Input/'+str(M_List[M])+'/'+Line
            os.mkdir(path)

            CamNum = int(TotalLineNCam[M][Line])
            try:
                for c in range(1, CamNum+1):
                    path='./DotDist_Input/'+str(M_List[M])+'/'+Line+'/Cam'+str(c)
                    os.mkdir(path)
            except:pass
                
        except:
            Line = TotalLineList[M][L]
            CamNum = int(TotalLineNCam[M][Line])
            try:
                for c in range(1, CamNum+1):
                    path='./DotDist_Input/'+str(M_List[M])+'/'+Line+'/Cam'+str(c)
                    os.mkdir(path)
            except:pass
            
print("\nInput folder Created!\n")
time.sleep(1)
##############################################################################################################################################
try:os.mkdir('./DotDist_Output')
except FileExistsError:pass

for M in range(len(M_List)):
    try:
        os.mkdir('./DotDist_Output/'+str(M_List[M]))
    except FileExistsError:
        pass

    for L in range(len(TotalLineList[M])):
        try:
            Line = TotalLineList[M][L]
            path='./DotDist_Output/'+str(M_List[M])+'/'+Line
            os.mkdir(path)
                
        except:pass
            
print("\nOutput folder Created!\n")
time.sleep(1)
##############################################################################################################################################
TotalValue = pd.DataFrame(columns = ['M_Number', 'Line', 'Cam_Number', 'Axis', 'Max-Min', 'Average', 'Variance', 'Standard_Deviation']) 
INDEX=0
##############################################################################################################################################
try:
    for M in range(len(M_List)):
        print("\n<<< {} >>>".format(M_List[M]))

        for L in range(len(TotalLineList[M])):
            Line = TotalLineList[M][L]
            print("<< {} >>".format(Line))

            path='./DotDist_Input/'+str(M_List[M])+'/'+Line

            CamNum = int(TotalLineNCam[M][Line])
            for c in range(1, CamNum+1):
                pathSave = './DotDist_Output/'+str(M_List[M])+'/'+Line
                path='./DotDist_Input/'+str(M_List[M])+'/'+Line+'/Cam'+str(c)

                for axis in ["X", "Y"]:
                    try:
                        file = path+"/-1Cam_Dist"+axis+".csv"
                        InputData = pd.read_csv(file)
                        InfoList = [M_List[M], Line, c, axis]
                        ValueList = list(ValueHandle(InputData))[3:]
                        TotalValue.loc[INDEX] = InfoList+ValueList
                        Name = "Cam"+str(c)+"_"+axis
                        HeatMap(InputData, Name, pathSave)
                    except:
                        pass
                    INDEX+=1
            TotalValue.loc[INDEX] = [None, None, None, None, None, None, None, None]
            INDEX+=1
        TotalValue.loc[INDEX] = [None, None, None, None, None, None, None, None]
        INDEX+=1
        
    print()
    LogSave("work", None)
        
except Exception as e:
    print()
    LogSave("fail", str(e)[10:])
    pass
##############################################################################################################################################
TotalValue.to_csv("./Total_Inspection_Value.csv", index=False)
##############################################################################################################################################
print("\n\n\nJob Done.")
time.sleep(5)
sys.exit()


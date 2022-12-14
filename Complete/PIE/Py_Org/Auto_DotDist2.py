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
################################################################################################
def HeatMap(Data, Name, Path):
    plt.figure(figsize=(60, 40))
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    sns.heatmap(Data, annot=True, fmt='.3f', annot_kws={"size": 25}, cmap='summer', cbar=False)
    plt.title(Name, pad=50, fontsize=50)
    plt.savefig(Path+"/"+Name+'.png')
    plt.close()
################################################################################################
def LogSave(Check, ErrorMsg):
    now = time
    startTime = now.strftime('%Y-%m-%d %H:%M:%S')
    #print(startTime)
    path='./'
    LogCheck = os.listdir(path)
    if "Log.txt" not in LogCheck:
        print("\nLog file Created!")
        file = open("./Log.txt", "w")
        file.write("<<DotDist Edit - Run Log>>")
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
################################################################################################    
def ValueHandle(InputData):
    data=InputData
    DfList=[]
    for n in range(len(data.columns)):
        columnsList = list(np.array(data[str(n)].tolist()))
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
################################################################################################
def INFO(YN):
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

        M = len(M_List)

        Result = [M, TotalLineList, TotalLineNCam]

        with open("SetInfo.pkl", 'wb') as f:
            pickle.dump(Result, f)

        return Result
                
    else:
        print("Exit.")
        sys.exit()
################################################################################################
YN = input("셋업 정보 저장 과정 실행 여부를 입력해주세요. (Y/N)\n>> ")
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
################################################################################################
print()
print(LoadInfo)

"""
여기서
# 이후 코드 실행에 필요한 인자들은 M, M들의 line별 리스트=TotalLineList의 소리스트,  각 line의 cam 수=TotalLineNCam의 소딕셔너리
"""

################################################################################################
M1Line = ["AA", "SV", "CA"]
M2Line = ["PA1", "PA2", "AA", "SV", "CA"]
M3Line = ["AA", "SV", "CA"]
################################################################################################
try:os.mkdir('./DotDist_Input')
except FileExistsError:pass

for M in range(1, 4):
    try:
        os.mkdir('./DotDist_Input/M'+str(M))
    except FileExistsError:
        pass
    
    if M==1:
        for folder in M1Line:
            try:
                path='./DotDist_Input/M1/'+folder
                os.mkdir(path)
                
                for c in range(1,4):
                    os.mkdir(path+'/Cam'+str(c))
                    
            except FileExistsError:
                pass
            
    elif M==2:
        for folder in M2Line:
            try:
                path='./DotDist_Input/M2/'+folder
                os.mkdir(path)
                
                if folder=="PA1" or folder=="PA2":
                    for c in range(1,3):
                        os.mkdir(path+'/Cam'+str(c))
                elif folder=="AA" or folder=="SV":
                    for c in range(1,4):
                        os.mkdir(path+'/Cam'+str(c))
                elif folder=="CA":
                    for c in range(1,6):
                        os.mkdir(path+'/Cam'+str(c))
                    
            except FileExistsError:
                pass
            
    elif M==3:
        for folder in M3Line:
            try:
                path='./DotDist_Input/M3/'+folder
                os.mkdir(path)

                for c in range(1,4):
                    os.mkdir(path+'/Cam'+str(c))
                    
            except FileExistsError:
                pass
            
print("\nInput folder Created!\n")
time.sleep(1)
################################################################################################
try:os.mkdir('./DotDist_Output')
except FileExistsError:pass

for M in range(1, 4):
    try:os.mkdir('./DotDist_Output/M'+str(M))
    except FileExistsError:pass

    if M==1:
        for folder in M1Line:
            try:
                path='./DotDist_Output/M1/'+folder
                os.mkdir(path)

            except FileExistsError:pass
###############################################
    elif M==2:
        for folder in M2Line:
            try:
                path='./DotDist_Output/M2/'+folder
                os.mkdir(path)

            except FileExistsError:pass
###############################################
    elif M==3:
        for folder in M3Line:
            try:
                path='./DotDist_Output/M3/'+folder
                os.mkdir(path)

            except FileExistsError:pass
            
print("Output folder Created!\n")
time.sleep(1)
################################################################################################
TotalValue = pd.DataFrame(columns = ['M_Number', 'Line', 'Cam_Number', 'Axis', 'Max-Min', 'Average', 'Variance', 'Standard_Deviation']) 
INDEX=0
################################################################################################
try:
    for M in range(1, 4):
        if M==1:
            print("\n<<< M1 >>>")
            for folder in M1Line:
                print("<< {} >>".format(folder))
                path='./DotDist_Output/M1/'+folder

                for camNum in range(1,4):
                    print("< cam{} >.".format(camNum))
                    oldVerPath = './DotDist_Output/M1/'+folder+"/Cam"+str(camNum)
                    path = './DotDist_Output/M1/'+folder
                    camCnt = len(os.listdir(path))

                    pathFront=oldVerPath[:10]
                    pathBack=oldVerPath[16:]
                    path_IN=pathFront+"Input"+pathBack

                    for axis in ["X", "Y"]:
                        try:
                            file = path_IN+"/-1Cam_Dist"+axis+".csv"
                            InputData = pd.read_csv(file)
                            InfoList = ["M"+str(M), folder, camNum, axis]
                            ValueList = list(ValueHandle(InputData))[3:]
                            TotalValue.loc[INDEX] = InfoList+ValueList
                            Name = "Cam"+str(camNum)+"_"+axis
                            HeatMap(InputData, Name, path)
                        except:
                            pass
                        INDEX+=1
                TotalValue.loc[INDEX] = [None, None, None, None, None, None, None, None]
                INDEX+=1
            TotalValue.loc[INDEX] = [None, None, None, None, None, None, None, None]
            INDEX+=1

    ##################################################
        elif M==2:
            print("\n<<< M2 >>>")
            for folder in M2Line:
                print("<< {} >>".format(folder))
                path='./DotDist_Output/M2/'+folder

                if folder=="PA1" or folder=="PA2":
                    camNum=2
                elif folder=="AA" or folder=="SV":
                    camNum=3
                elif folder=="CA":
                    camNum=5

                for cam in range(1, camNum+1):
                    print("< cam{} >.".format(cam))
                    oldVerPath = './DotDist_Output/M2/'+folder+"/Cam"+str(cam)
                    path = './DotDist_Output/M2/'+folder
                    camCnt = len(os.listdir(path))

                    pathFront=oldVerPath[:10]
                    pathBack=oldVerPath[16:]
                    path_IN=pathFront+"Input"+pathBack

                    for axis in ["X", "Y"]:
                        try:
                            file = path_IN+"/-1Cam_Dist"+axis+".csv"
                            InputData = pd.read_csv(file)
                            InfoList = ["M"+str(M), folder, cam, axis]
                            ValueList = list(ValueHandle(InputData))[3:]
                            TotalValue.loc[INDEX] = InfoList+ValueList
                            Name = "Cam"+str(cam)+"_"+axis
                            HeatMap(InputData, Name, path)
                        except:
                            pass
                        INDEX+=1
                TotalValue.loc[INDEX] = [None, None, None, None, None, None, None, None]
                INDEX+=1
            TotalValue.loc[INDEX] = [None, None, None, None, None, None, None, None]
            INDEX+=1
    ##################################################      
        elif M==3:
            print("\n<<< M3 >>>")
            for folder in M3Line:
                print("<< {} >>".format(folder))
                path='./DotDist_Output/M3/'+folder

                for camNum in range(1,4):
                    print("< cam{} >.".format(camNum))
                    oldVerPath = './DotDist_Output/M3/'+folder+"/Cam"+str(camNum)
                    path = './DotDist_Output/M3/'+folder
                    camCnt = len(os.listdir(path))

                    pathFront=oldVerPath[:10]
                    pathBack=oldVerPath[16:]
                    path_IN=pathFront+"Input"+pathBack

                    for axis in ["X", "Y"]:
                        try:
                            file = path_IN+"/-1Cam_Dist"+axis+".csv"
                            InputData = pd.read_csv(file)
                            InfoList = ["M"+str(M), folder, camNum, axis]
                            ValueList = list(ValueHandle(InputData))[3:]
                            TotalValue.loc[INDEX] = InfoList+ValueList
                            Name = "Cam"+str(camNum)+"_"+axis
                            HeatMap(InputData, Name, path)
                        except:
                            pass
                        INDEX+=1

                TotalValue.loc[INDEX] = [None, None, None, None, None, None, None, None]
                INDEX+=1
    LogSave("work", None)
except Exception as e:
    LogSave("fail", str(e)[10:])
    pass
################################################################################################ 
TotalValue.to_csv("./Total_Inspection_Value.csv", index=False)
################################################################################################ 
print("\n\n\nJob Done.")
time.sleep(5)


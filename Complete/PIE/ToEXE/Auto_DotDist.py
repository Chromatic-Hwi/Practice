import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import os
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
        print("Log file no exist!")
        file = open("./Log.txt", "w")
        file.write("<<DotDist Edit - Run Log>>")
        file.close
    else:
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
################################################################################################
TotalValue = pd.DataFrame(columns = ['M_Number', 'Line', 'Cam_Number', 'Axis', 'Max-Min', 'Average', 'Variance', 'Standard_Deviation']) 
INDEX=0
################################################################################################
try:
    for M in range(1, 4):
        if M==1:
            print("M1")
            for folder in M1Line:
                path='./DotDist_Output/M1/'+folder

                for camNum in range(1,4):
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
            print("M2")
            for folder in M2Line:
                path='./DotDist_Output/M2/'+folder

                if folder=="PA1" or folder=="PA2":
                    camNum=2
                elif folder=="AA" or folder=="SV":
                    camNum=3
                elif folder=="CA":
                    camNum=5

                for cam in range(1, camNum+1):
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
            print("M3")
            for folder in M3Line:
                path='./DotDist_Output/M3/'+folder

                for camNum in range(1,4):
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
#sys.exit()

LoadInfo=[['M1_1', 'M1_2', 'M2', 'M3'], [['AA', 'CA', 'SV'], ['AA', 'CA', 'SV'], ['PA1', 'PA2', 'AA', 'CA', 'SV'], ['AA', 'CA', 'SV']], [{'AA': '3', 'CA': '3', 'SV': '3'}, {'AA': '3', 'CA': '3', 'SV': '3'}, {'PA1': '2', 'PA2': '2', 'AA': '3', 'CA': '5', 'SV': '3'}, {'AA': '3', 'CA': '3', 'SV': '3'}]]

M_List = LoadInfo[0]
TotalLineList = LoadInfo[1]
TotalLineNCam = LoadInfo[2]

M = 2
c = 0
Line = TotalLineList[M]
print(Line)

for c in range(len(Line)):
    print(Line[c])
    print(TotalLineNCam[M][Line[c]])

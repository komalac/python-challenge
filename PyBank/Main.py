import os
import csv

DTList= []
PLList = []
TotPL = 0
PLChgList = []

filepath = os.path.join("Resources", "budget_data.csv")
with open(filepath, newline="") as BdgDataFile:
    
    ReadBdgData = csv.reader(BdgDataFile)    
    for row in ReadBdgData:
        DTList.append(row[0])
        PLList.append(row[1])

    del PLList[0]
    del DTList[0]
    PrevChg = int(PLList[0])
    PLChg = 0
    TotChg = 0


    LLength = len(PLList)
    
    for pl in range(LLength):
        TotPL = TotPL + int(PLList[pl])  
        PLChg = int(PLList[pl]) - PrevChg
        PLChgList.append(PLChg)
        TotChg = TotChg + PLChg
        PrevChg = int(PLList[pl])
        

    LLength = LLength - 1
    maxPL = max(PLChgList) 
    maxPLDate = PLChgList.index(maxPL)
    minPL = min(PLChgList) 
    minPLDate = PLChgList.index(minPL)
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(PLList)}")
    print(f"Total: {TotPL}")
    print(f"Average  Change: ${round(TotChg/LLength, 2)}")
    print(f"Greatest Increase in Profits: {DTList[maxPLDate]} (${maxPL})")
    print(f"Greatest Decrease in Profits: {DTList[minPLDate]} (${minPL})")

OPfile = open("output.txt", "w")
OPfile.write("Financial Analysis\n")
OPfile.write("----------------------------\n")
OPfile.write(f"Total Months: {len(PLList)}\n")
OPfile.write(f"Total: {TotPL}\n")
OPfile.write(f"Average  Change: ${round(TotChg/LLength, 2)}\n")
OPfile.write(f"Greatest Increase in Profits: {DTList[maxPLDate]} (${maxPL})\n")
OPfile.write(f"Greatest Decrease in Profits: {DTList[minPLDate]} (${minPL})\n")
OPfile.close()


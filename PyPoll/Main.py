import os
import csv

VIDList= []
CountyList = []
CandidateList = []
VoteCount = []

filepath = os.path.join("Resources", "election_data.csv")
with open(filepath, newline="") as ElecDataFile:
    ReadElecData = csv.reader(ElecDataFile)    

    for row in ReadElecData:
        VIDList.append(row[0])
        CountyList.append(row[1])
        CandidateList.append(row[2])

    del VIDList[0]
    del CountyList[0]
    del CandidateList[0]

    TotVote = len(VIDList)
    
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {TotVote}")
    print("-------------------------")
    

    OPfile = open("output.txt", "w")
    OPfile.write("Election Results\n")
    OPfile.write("-------------------------\n")
    OPfile.write(f"Total Votes: {TotVote}\n")
    OPfile.write("-------------------------\n")


    CanSet = set(CandidateList)
    UniCandidateList = list(CanSet)
    CLLength = len(UniCandidateList)
    UCLLength = len(CandidateList)

    for ucl in range(CLLength):
        CanTotVote = 0
        TotNumVote = 0
        for cl in range(UCLLength):
            if CandidateList[cl] == UniCandidateList[ucl]:
                CanTotVote = CanTotVote + 1

        VoteCount.append(CanTotVote)    
        print(f"{UniCandidateList[ucl]}: {round((CanTotVote/TotVote)*100, 2)}% ({CanTotVote})")
        OPfile.write(UniCandidateList[ucl] + ": " + str(round((CanTotVote/TotVote)*100, 2)) + "% (" + str(CanTotVote) + ")\n")
        
    MaxVote   = max(VoteCount)
    WinnerCnd = VoteCount.index(MaxVote)
    print("-------------------------")
    print(f"Winner: {UniCandidateList[WinnerCnd]}")
    print("-------------------------")
      
    OPfile.write("-------------------------\n")
    OPfile.write("Winner: " + UniCandidateList[WinnerCnd])
    OPfile.write("\n-------------------------\n")
  
  
 
        
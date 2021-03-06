import os
import csv

#Declaring all lists
VIDList= []
CountyList = []
CandidateList = []
VoteCount = []

#Opening csv file
filepath = os.path.join("Resources", "election_data.csv")
with open(filepath, newline="") as ElecDataFile:
    ReadElecData = csv.reader(ElecDataFile)    
    
    #creating list for each column
    for row in ReadElecData:
        VIDList.append(row[0])
        CountyList.append(row[1])
        CandidateList.append(row[2])

    #deleting header row
    del VIDList[0]
    del CountyList[0]
    del CandidateList[0]

    TotVote = len(VIDList)
    
    #printing in terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {TotVote}")
    print("-------------------------")
    
    #Opening the output file
    OPfile = open("output.txt", "w")

    #writing into the output file
    OPfile.write("Election Results\n")
    OPfile.write("-------------------------\n")
    OPfile.write(f"Total Votes: {TotVote}\n")
    OPfile.write("-------------------------\n")

    #Unique Candidate names
    CanSet = set(CandidateList)
    UniCandidateList = list(CanSet)

    UCLLength = len(UniCandidateList)
    CLLength = len(CandidateList)

    #looping through the unique lists, nested with the main candidate list
    for ucl in range(UCLLength):
        CanTotVote = 0
        TotNumVote = 0
        for cl in range(CLLength):
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
  
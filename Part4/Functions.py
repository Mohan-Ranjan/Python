# Create Variables
CountTotal = 0
CountProgress = 0
CountTrailer = 0
CountRetriever = 0
CountExcluded = 0
List = []
ProgressList = []
TrailerList = []
RetrieverList = []
ExcludedList = []
IndexProgress = 0
IndexTrailer = 0
IndexRetriever = 0
IndexExcluded = 0

# Define Validation
def Validation():
    global CountTotal
    global CountProgress
    global CountTrailer
    global CountRetriever
    global CountExcluded
    global List
    global IndexProgress
    global IndexTrailer
    global IndexRetriever
    global IndexExcluded
    global ProgressList
    global TrailerList
    global RetrieverList
    global ExcludedList
    try:
        fo=open("Data.txt","w")
        CountNumber = 0
        print("Volume of Credit at Each Level")
        Pass = int(input("Please enter your credits at Pass : "))
        fo.write("Pass")
        List.insert(CountNumber,Pass)
        while Pass not in range(0,130,20):
            print("Out of Range")
            Pass = int(input("Please enter your credits at Pass : "))
            fo.write("Pass")
            List.insert(CountNumber,Pass)
        else:
            Defer = int(input("Please enter your credits at Defer : "))
            fo.write("Defer")
            CountNumber = CountNumber + 1
            List.insert(CountNumber,Defer)
            while Defer not in range(0,130,20):
                print("Out of Range")
                Defer = int(input("Please enter your credits at Defer : "))
                fo.write("Defer")
                List.insert(CountNumber,Defer)
            else:
                Fail = int(input("Please enter your credits at Fail : "))
                fo.write("Fail")
                CountNumber = CountNumber + 1
                List.insert(CountNumber,Fail)
                while Fail not in range(0,130,20):
                    print("Out of Range")
                    Fail = int(input("Please enter your credits at Fail : "))
                    fo.write("Fail")
                    List.insert(CountNumber,Fail)
                else:
                    if Pass+Defer+Fail == 120 :
                        if (Pass == 120):
                            print("Progress")
                            fo.write("Progress")
                            CountTotal = CountTotal + 1
                            ProgressList.insert(IndexProgress,List)
                            List = []
                            IndexProgress = IndexProgress + 1
                            CountProgress += 1
                        elif (Pass == 100): 
                            print("Progress (Module Trailer)")
                            fo.write("Progress (Module Trailer)")
                            CountTotal += 1
                            TrailerList.insert(IndexTrailer,List)
                            List = []
                            IndexTrailer += 1
                            CountTrailer += 1
                        elif Pass<=80 and Pass>=0 and Fail<=60 : 
                            print("Do not Progress – module Retriever")
                            fo.write("Do not Progress – module Retriever")
                            CountTotal += 1
                            RetrieverList.insert(IndexRetriever,List)
                            List = []
                            IndexRetriever += 1
                            CountRetriever += 1
                        elif Pass<=40 and Pass>=0 and Defer<=40:
                            print("Exclude")
                            fo.write("Exclude")
                            CountTotal += 1
                            ExcludedList.insert(IndexExcluded,List)
                            List = []
                            IndexExcluded += 1
                            CountExcluded += 1
                    else:
                        print("Total Incorrect")
                        fo.write("Total Incorrect")
    except():
        print("Integer Required")
        fo.write("Integer Required")
    fo.close()
    

    
# Horizontal Histogam
def HorizontalHistogram():
    fo=open("Data.txt","w")
    Star="*"
    print("---------------------------------------------------------------")
    fo.write("---------------------------------------------------------------")
    print("Horizontal Histogram")
    fo.write("Horizontal Histogram")
    print("Progress    - ",CountProgress,":",(CountProgress*Star))
    fo.write("'Progress    - ',CountProgress,':',(CountProgress*Star)")
    print("Trailer     - ",CountTrailer,":",(CountTrailer*Star))
    fo.write("'Trailer     - ',CountTrailer,':',(CountTrailer*Star)")
    print("Rretriever  - ",CountRetriever,":",(CountRetriever*Star))
    fo.write("'retriever  - ',CountRetriever,':',(CountRetriever*Star)")
    print("Excluded    - ",CountExcluded,":",(CountExcluded*Star))
    fo.write("'Excluded    - ',CountExcluded,':',(CountExcluded*Star)")
    print()
    fo.write(" ")
    print()
    fo.write(" ")
    print(CountTotal,"outcomes in total")
    fo.write("CountTotal,'outcomes in total'")
    print("---------------------------------------------------------------")
    fo.write("---------------------------------------------------------------")
    fo.close()
    
# Vertical Histogram
def VerticalHistogram ():
    fo=open("Data.txt","w")
    global CountTotal
    global CountProgress
    global CountTrailer
    global CountRetriever
    global CountExcluded
    Star="*"
    Space=" "
    Row1=""
    Row2=""
    Row3=""
    Row4=""
    print("Vertical Histogram")
    fo.write("Vertical Histogram")
    print ("Progress","Trailer","Retriever","Excluded")
    fo.write("'Progress','Trailer','Retriever','Excluded'")
    while CountTotal != 0:
        if CountProgress > 0 :
            Row1=(Space*3+"*")
            CountProgress -= 1
        else:
            Row1=(Space*4)
        if CountTrailer > 0:
            Row2=(Space*7+"*")
            CountTrailer -= 1
        else:
            Row2=(Space*8)
        if CountRetriever > 0:
            Row3=(Space*7+"*")
            CountRetriever -= 1
        else:
            Row3=(Space*8)
        if CountExcluded > 0:
            Row4=(Space*7+"*")
            CountExcluded -= 1
        else:
            Row4=(Space*8)
        print(Row1,Row2,Row3,Row4)
        fo.write("Row1,Row2,Row3,Row4")
        CountTotal = CountTotal - 1    
        
    print("---------------------------------------------------------------")
    fo.write("---------------------------------------------------------------")
    fo.close()

# Display in List
def DisplayInList():
    f=open("Data.txt","w")
    global IndexProgress
    global IndexTrailer
    global IndexRetriever
    global IndexExcluded
    global ProgressList
    global TrailerList
    global RetrieverList
    global ExcludedList
    global CountTotal

    i = 0
    
    for i in range(len(ProgressList)):
        print("Progress - ",ProgressList[i])
        f.write("'Progress - ',ProgressList[i]")
    i = 0
    for i in range(len(TrailerList)):
        print("Progress (Module Trailer) - ",TrailerList[i])
        f.write("'Progress (Module Trailer) - ',TrailerList[i]")
    i = 0
    for i in range(len(RetrieverList)):
        print("Do not Progress (Module Retriever) - ",RetrieverList[i])
        f.write("'Do not Progress (Module Retriever) - ',RetrieverList[i]")
    i = 0
    for i in range(len(ExcludedList)):
        print("Exclude - ",ExcludedList[i])
        f.write("'Exclude - ',ExcludedList[i]")
    f.close()
    

               

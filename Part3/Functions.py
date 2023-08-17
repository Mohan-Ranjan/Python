# Create Variables
CountTotal = 0
CountProgress = 0
CountTrailer = 0
CountRetriever = 0
CountExcluded = 0
# Create List
List = []
ProgressList = []
TrailerList = []
RetrieverList = []
ExcludedList = []
IndexProgress = 0
IndexTrailer = 0
IndexRetriever = 0
IndexExcluded = 0

# Definr the Validation
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
        CountNumber = 0
        print("Volume of Credit at Each Level")
        Pass = int(input("Please enter your credits at Pass : "))
        # Insert into List
        List.insert(CountNumber,Pass)
        while Pass not in range(0,130,20):
            print("Out of Range")
            Pass = int(input("Please enter your credits at Pass : "))
            List.insert(CountNumber,Pass)
        else:
            Defer = int(input("Please enter your credits at Defer : "))
            CountNumber = CountNumber + 1
            List.insert(CountNumber,Defer)
            while Defer not in range(0,130,20):
                print("Out of Range")
                Defer = int(input("Please enter your credits at Defer : "))
                List.insert(CountNumber,Defer)
            else:
                Fail = int(input("Please enter your credits at Fail : "))
                CountNumber = CountNumber + 1
                List.insert(CountNumber,Fail)
                while Fail not in range(0,130,20):
                    print("Out of Range")
                    Fail = int(input("Please enter your credits at Fail : "))
                    List.insert(CountNumber,Fail)
                else:
                    if Pass+Defer+Fail == 120 :
                        
                        if (Pass == 120):
                            
                            print("Progress")
                            CountTotal = CountTotal + 1
                            # Insert into List
                            ProgressList.insert(IndexProgress,List)
                            List = []
                            IndexProgress = IndexProgress + 1
                            CountProgress += 1
                        elif (Pass == 100):
                             
                            print("Progress (Module Trailer)")
                            CountTotal += 1
                            TrailerList.insert(IndexTrailer,List)
                            List = []
                            IndexTrailer += 1
                            CountTrailer += 1
                        elif Pass<=80 and Pass>=0 and Fail<=60 :
                             
                            print("Do not Progress – module Retriever")
                            CountTotal += 1
                            RetrieverList.insert(IndexRetriever,List)
                            List = []
                            IndexRetriever += 1
                            CountRetriever += 1
                        elif Pass<=40 and Pass>=0 and Defer<=40:
                            
                            print("Exclude")
                            CountTotal += 1
                            ExcludedList.insert(IndexExcluded,List)
                            List = []
                            IndexExcluded += 1
                            CountExcluded += 1
                    else:
                        print("Total Incorrect")
    except():
        print("Integer Required")

    
# Define Horizontal Histogram
def HorizontalHistogram():
    Star="*"
    print("---------------------------------------------------------------")
    print("Horizontal Histogram")
    print("Progress    - ",CountProgress,":",(CountProgress*Star))
    print("Trailer     - ",CountTrailer,":",(CountTrailer*Star))
    print("Rretriever  - ",CountRetriever,":",(CountRetriever*Star))
    print("Excluded    - ",CountExcluded,":",(CountExcluded*Star))
    print()
    print()
    print(CountTotal,"outcomes in total")
    print("---------------------------------------------------------------")
    
# Define Vertical Histogram
def VerticalHistogram ():
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
    print ("Progress","Trailer","Retriever","Excluded")
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
        CountTotal = CountTotal - 1    
    
        
    print("---------------------------------------------------------------")

# Define in the List
def DisplayInList():
    global IndexProgress
    global IndexTrailer
    global IndexRetriever
    global IndexExcluded
    global ProgressList
    global TrailerList
    global RetrieverList
    global ExcludedList
    global CountTotal

# Output the List
    i = 0
    for i in range(len(ProgressList)):
        # Print the List
        print("Progress - ",ProgressList[i])
    i = 0
    for i in range(len(TrailerList)):
        print("Progress (Module Trailer) - ",TrailerList[i])
    i = 0
    for i in range(len(RetrieverList)):
        print("Do not Progress (Module Retriever) - ",RetrieverList[i])
    i = 0
    for i in range(len(ExcludedList)):
        print("Exclude - ",ExcludedList[i])
    
    

               

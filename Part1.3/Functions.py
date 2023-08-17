# Create Variables
CountTotal = 0
CountProgress = 0
CountTrailer = 0
CountRetriever = 0
CountExcluded = 0

# Define Functions
def Validation():
    global CountTotal
    global CountProgress
    global CountTrailer
    global CountRetriever
    global CountExcluded
    try:
        # Input with try exception part
        print("Volume of Credit at Each Level")
        Pass = int(input("Please enter your credits at Pass : "))
        while Pass not in range(0,130,20):
            print("Out of Range")
            Pass = int(input("Please enter your credits at Pass : "))
        else:
            Defer = int(input("Please enter your credits at Defer : "))
            while Defer not in range(0,130,20):
                print("Out of Range")
                Defer = int(input("Please enter your credits at Defer : "))
            else:
                Fail = int(input("Please enter your credits at Fail : "))
                while Fail not in range(0,130,20):
                    print("Out of Range")
                    Fail = int(input("Please enter your credits at Fail : "))
                else:
                    if Pass+Defer+Fail == 120 :
                        # Main Outcomes
                        if (Pass == 120):
                            print("Progress")
                            CountTotal = CountTotal + 1
                            CountProgress += 1 
                        elif (Pass == 100):
                            print("Progress (Module Trailer)")
                            CountTotal += 1
                            CountTrailer += 1
                        elif Pass<=80 and Pass>=0 and Fail<=60 :
                            print("Do not Progress – module retriever")
                            CountTotal += 1
                            CountRetriever += 1
                        elif Pass<=40 and Pass>=0 and Defer<=40:
                            print("Exclude")
                            CountTotal += 1
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
    
    


               

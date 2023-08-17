# Create Variables
CountTotal = 0
CountProgress = 0
CountTrailer = 0
CountRetriever = 0
CountExcluded = 0

# Define Variables
def Validation():
    # Global Variables
    global CountTotal
    global CountProgress
    global CountTrailer
    global CountRetriever
    global CountExcluded
    try:
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

    
# Definr the Horizontal Histogram
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
    # Global Variables
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
    print(CountTotal,"outcomes in total")
    # Put Headings
    print ("Progress","Trailer","Retriever","Excluded")
    # Print Stars
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
        # Output
        print(Row1,Row2,Row3,Row4)
        # Increment or Update Variable
        CountTotal = CountTotal - 1
    
    print("---------------------------------------------------------------")



               

# CourseWork
# Part 1.1
# Create Variables
Pass = 0
Defer = 0
Fail = 0

# Input Variables
print("Volume of Credit at Each Level")
Pass = int(input("Please enter your credits at Pass : "))
Defer = int(input("Please enter your credits at Defer : "))
Fail = int(input("Please enter your credits at Fail : "))

#Process    
# 1 Condition
if (Pass == 120):
    if (Defer == 0):
        if (Fail == 0):
            #Output
            print("Progress")
# 2 Condition
elif(Pass == 100):
    if (Defer == 20):
        if (Fail == 0):
            #Output
            print("Progress (Module Trailer)")
    elif (Defer == 0):
        if (Fail == 20):
            #Output
            print("Progress (Module Trailer)")
# 4 Condition
elif(Pass == 80):
    if (Defer == 40):
        if (Fail == 0):
            #Output
            print("Do not Progress - Module Retriever")
    elif (Defer == 20):
        if (Fail == 20):
            #Output
            print("Do not Progress - Module Retriever")
    elif (Defer == 0):
        if (Fail == 40):
            #Output
            print("Do not Progress - Module Retriever")
# 7 Condition
elif(Pass == 60):
    if (Defer == 60):
        if (Fail == 0):
            #Output
            print("Do not Progress - Module Retriever")
    elif (Defer == 40):
        if (Fail == 20):
            #Output
            print("Do not Progress - Module Retriever")
    elif (Defer == 20):
        if (Fail == 40):
            #Output
            print("Do not Progress - Module Retriever")
    elif (Defer == 0):
        if (Fail == 60):
            #Output
            print("Do not Progress - Module Retriever")
# 11 Condition
elif(Pass == 40):
    if (Defer == 80):
        if (Fail == 0):
            #Output
            print("Do not Progress - Module Retriever")
    elif (Defer == 60):
        if (Fail == 20):
            #Output
            print("Do not Progress - Module Retriever")
    elif (Defer == 40):
        if (Fail == 40):
            #Output
            print("Do not Progress - Module Retriever")
    elif (Defer == 20):
        if (Fail == 60):
            #Output
            print("Do not Progress - Module Retriever")
    elif (Defer == 0):
        if (Fail == 80):
            #Output
            print("Exclude")
# 16 Condition
elif(Pass == 20):
    if (Defer == 100):
        if (Fail == 0):
            #Output
            print("Do not Progress - Module Retriever")
    elif (Defer == 80):
        if (Fail == 20):
            #Output
            print("Do not Progress - Module Retriever")
    elif (Defer == 60):
        if (Fail == 40):
            #Output
            print("Do not Progress - Module Retriever")
    elif (Defer == 40):
        if (Fail == 60):
            #Output
            print("Do not Progress - Module Retriever")
    elif (Defer == 20):
        if (Fail == 80):
            #Output
            print("Exclude")
    elif (Defer == 0):
        if (Fail == 100):
            #Output
            print("Exclude")
# 22 Condition
elif(Pass == 0):
    if (Defer == 120):
        if (Fail == 0):
            #Output
            print("Do not Progress - Module Retriever")
    elif (Defer == 100):
        if (Fail == 20):
            #Output
            print("Do not Progress - Module Retriever")
    elif (Defer == 80):
        if (Fail == 40):
            #Output
            print("Do not Progress - Module Retriever")
    elif (Defer == 60):
        if (Fail == 60):
            #Output
            print("Do not Progress - Module Retriever")
    elif (Defer == 40):
        if (Fail == 80):
            #Output
            print("Exclude")
    elif (Defer == 20):
        if (Fail == 100):
            #Output
            print("Exclude")
    elif (Defer == 0):
        if (Fail == 120):
            #Output
            print("Exclude")

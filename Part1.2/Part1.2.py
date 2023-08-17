# Coursework
# Part 1.2
# Create Variables
Pass = 0
Defer = 0
Fail = 0

# Use Try Exception Handler
try:   
    print("Volume of Credit at Each Level")
    # Input Pass Variable
    Pass = int(input("Please enter your credits at Pass : "))
    while Pass not in range(0,130,20):
        # Output part of out of range
        print("Out of Range")
        # Again Input Variable
        Pass = int(input("Please enter your credits at Pass : "))
    else:
        # Input Defer Variable
        Defer = int(input("Please enter your credits at Defer : "))
        while Defer not in range(0,130,20):
            print("Out of Range")
            Defer = int(input("Please enter your credits at Defer : "))
        else:
            # Input Fail Variable
            Fail = int(input("Please enter your credits at Fail : "))
            while Fail not in range(0,130,20):
                print("Out of Range")
                Fail = int(input("Please enter your credits at Fail : "))
            else:
                # Check Sum of the variables equal to 120
                if Pass+Defer+Fail == 120 :
                    # Conditions Output
                    if (Pass == 120):
                        print("Progress")
                    elif (Pass == 100):
                        print("Progress (Module Trailer)")
                    elif Pass<=80 and Pass>=0 and Fail<=60 :
                        print("Do not Progress – module retriever")
                    elif Pass<=40 and Pass>=0 and Defer<=40:
                        print("Exclude")        
                else:
                    # Output
                    print("Total Incorrect")
except:
    # Print output using except
    print("Integer Required")

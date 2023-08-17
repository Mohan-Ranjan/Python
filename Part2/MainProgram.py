# Import Functions
import Functions

# Staff Version
print("Staff Version with Histogram")
# Calling Function
Functions.Validation()
# Input Variable
Continuation = input("Would you like to enter another set of data?\n"
                  "Enter 'y' for yes or 'q' to quit and view results : ")
Continuation = Continuation.lower()
# Selection for more inputs and outputs
while ((Continuation == "q") or (Continuation == "y" )):
    if (Continuation == "y"):
        #  Calling Validating Function
        Functions.Validation()
        # Again Input
        Continuation = input("Would you like to enter another set of data?\n"
                  "Enter 'y' for yes or 'q' to quit and view results : ")
        Continuation = Continuation.lower()
    # Exit loop
    elif (Continuation == "q"):
        Functions.HorizontalHistogram()
        Functions.VerticalHistogram ()
        break
    else:
        print("Invalid Option") 

# End of Program

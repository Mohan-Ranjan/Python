# Import Functions
import Functions

# Calling Function
print("Staff Version with Histogram")
Functions.Validation()
Continuation = input("Would you like to enter another set of data?\n"
                  "Enter 'y' for yes or 'q' to quit and view results : ")
Continuation = Continuation.lower()
while ((Continuation == "q") or (Continuation == "y" )):
    if (Continuation == "y"):
        Functions.Validation()
        Continuation = input("Would you like to enter another set of data?\n"
                  "Enter 'y' for yes or 'q' to quit and view results : ")
        Continuation = Continuation.lower()
    elif (Continuation == "q"):
        Functions.HorizontalHistogram()
        Functions.VerticalHistogram ()
        # Calling the List
        Functions.DisplayInList()
        break
    else:
        print("Invalid Option") 

# End of Program

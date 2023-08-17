# Import Functions
import Functions

# Staff Version
print("Staff Version with Histogram")
# Calling Functions
Functions.Validation()
# Input Variable
Continuation = input("Would you like to enter another set of data?\n"
                  "Enter 'y' for yes or 'q' to quit and view results : ")
Continuation = Continuation.lower()

# Optional Selections
while ((Continuation == "q") or (Continuation == "y" )):
    if (Continuation == "y"):
        # Calling Validation Part
        Functions.Validation()
        # Again Option
        Continuation = input("Would you like to enter another set of data?\n"
                  "Enter 'y' for yes or 'q' to quit and view results : ")
        Continuation = Continuation.lower()
    elif (Continuation == "q"):
        # Quit with Horizontal Histogram
        Functions.HorizontalHistogram()
        break
    else:
        # Invalid Options
        print("Invalid Option") 

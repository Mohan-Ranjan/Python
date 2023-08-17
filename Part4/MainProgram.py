# Import Functions
import Functions
# Create Variables
fo = 0
f = 0
# Open File
fo = open("Data.txt","w")

print("Staff Version with Histogram")
# Write on file
fo.write(("Staff Version with Histogram"))
Functions.Validation()
Continuation = input("Would you like to enter another set of data?\n"
                  "Enter 'y' for yes or 'q' to quit and view results : ")
fo.write(('Continuation'))
Continuation = Continuation.lower()
while ((Continuation == "q") or (Continuation == "y" )):
    if (Continuation == "y"):
        Functions.Validation()
        Continuation = input("Would you like to enter another set of data?\n"
                  "Enter 'y' for yes or 'q' to quit and view results : ")
        fo.write(Continuation)
        Continuation = Continuation.lower()
    elif (Continuation == "q"):
        Functions.HorizontalHistogram()
        Functions.VerticalHistogram ()
        Functions.DisplayInList()
        break
    else:
        print("Invalid Option")
        fo.write(("Invalid Option"))
# Close Files
fo.close()

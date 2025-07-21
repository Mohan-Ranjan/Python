#----------- Question 01.  ------------------------------------------------------------------------------------------------------
#-------- Qualify from the preliminary stage into the final stage for the Cycle Race. -------------------------------------------
#---- Create and Initialize the variables.  -------------------------------------------------------------------------------------
test=0
count=0

#----------- Input data of the medical test. ------------------------------------------------------------------------------------
test=int(input("Are you passed the Medical Test? (1/0): "))

if(test==1):
    print("Eligible to go for the ten rounds")
#---# input completed rounds. --------------------------------------------------------------------------------------------------- 
    count=int(input("How many rounds you completed in Ten(10) rounds? : "))
    if (count>=10):
           print("Best Regards, \nYou are qualify from preliminary stage into the final stage \nand eligible to the Cycle Race.")
    elif (count<10):
           print("Sorry, \nyou are  not eligible for the final stage \nBetter try Next time.") 
elif(test==0):
        print("Not allowed to attempt the ten rounds in the track")
elif(test==2 or 3 or  4 or 5 or 6 or 7 or 8 or 9) :
        print("if you are not took the medical test, \nYou can go and take it otherwise Not qualify for the ten rounds. ")  

#----------------------------------------- End of a programme --------------------------------------------------------------------

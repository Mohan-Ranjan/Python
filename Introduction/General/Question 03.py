#-------- Question 03. -----------------------------------------
#------ Evaluate the Body Mass Index(BMI). ---------------------
#-------------- Creating and Initializing variables. -----------
bmi=0
height=0
weight=0

#-------------- Input the Height(m) and Weight(kg) -------------
weight=float(input("Enter the Weight in kilograms : "))
height=float(input("Enter the Height in meters : "))

#------------ Calculating BMI ----------------------------------
bmi=weight/(height*height)

# ------ Display BMI -------------------------------------------
print("Body Mass Index :%0.2f"%bmi)
if (bmi<18.5):
    print("Under Weight")
elif (18.5<bmi<24.9):
    print("Normal")
elif (25<bmi<29):
    print("Over Weight")
elif (30<bmi):
    print("Obese")

#--------------  End of a programme --------------------------

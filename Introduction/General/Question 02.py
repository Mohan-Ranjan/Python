#---------- Question 02. --------------------------------------------------------------
#--------- Display surface area, volume and base area of the cone. ---------------------
#------- Creating and Initializing variables. ------------------------------------------
r=0
h=0
l=0
bac=0
sac=0
vc=0
option=""
pi=3.14

#------ Input Values for the calculation. -----------------------------------------------
print("Input the Radius(r),Height(h) and Slant Height(l) in same unit(m or cm) only.")
r=float(input("Radius(r) : "))
h=int(input("Height(h) : "))
l=int(input("Slant Height(l) : "))
option=input("Type an Option(A/S/V/B)Required : ")

#---- Calculating for the Surface Area(sac), Volume(vc) and Base Area(bac) of cone. -----
bac=(pi*r**2)
sac=(pi*r**2) + (pi*r*l)
vc=(1/3) * (pi*r**2) * h

#------------ Display the Surface Area, Volume and Base Area. ---------------------------
if (option=="A"):
    print("Base Area of a Cone : ",bac)
    print("Surface Arae of a Cone : ",sac)
    print("Volume of a Cone : ",vc)
elif(option=="S"):
    print("Surface Area of a Cone : ",sac)
elif(option=="V"):
    print("Volume of a Cone : ",vc)
elif(option=="B"):
    print("Base Area of a Cone : ",bac)
else:
    print("Invalid Option")

#------------------------ End of programme  ----------------------------------------------

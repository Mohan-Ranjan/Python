test=0
count=0

test= int(input("Sit for Medical test (1/0) : "))

if (test == 1):
    print("Allow to ten rounds")
    count = int(input ("No of rounds finished: "))
    if (count == 10):
       print("eligible")
    else:
        print("not eligible")
else :
    print ("Not eligible")

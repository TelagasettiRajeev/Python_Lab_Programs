days = int(input("Enter no.of days : "))

fine = 0
if( days>0 and days<=6 ):
    fine = 0.50
    print("You have to pay fine , Rs." , fine )
elif( days>6 and days<=15 ):
    fine = 1
    print("You have to pay fine , Rs." , fine )
elif( days>15 and days<=30 ):
    fine = 5
    print("You have to pay fine , Rs." , fine )
elif( days>30 ):
    print("Membership cancelled")
    

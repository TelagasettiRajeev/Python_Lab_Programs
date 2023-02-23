# formula : f = (c * 9)/5 + 32 and c = (f - 32)*5/9

choice = int(input("1 - convert from fahrenheit to celsius\n2 - convert from celsius to fahrenheit\nEnter your choice: "))

if( choice == 1 ):
    f = float(input("Enter the temperature in fahrenheit: "))
    c = (f - 32)*5/9
    print("Temperature in celsius : " , c )

elif( choice == 2 ):
    c = float(input("Enter the temperature in celsius : "))
    f = (c * 9)/5 + 32
    print("Temperature in fahrenheit : " , f )

else:
    print("Please check the correct option!")
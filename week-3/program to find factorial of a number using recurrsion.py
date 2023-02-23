n = int(input("Enter n : "))

if( n<0 ):
    print("Invalid number")
elif( n==0 ):
    print("Factorial of 0 is 1")
else:
    mul = 1
    for i in range(1, n+1 ):
        mul = mul * i
    print("Factorial of {} is {}".format(n, mul) )
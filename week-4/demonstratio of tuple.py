T = ("python", "java", "Kotlin","Ruby","Scala","Swift")
print("Created Tuple : " , T )

print("second language in tuple : ", T[1] )

print("From 3 - 6 languages are " , T[3:6] )

print("List of all items in tuple : ")
for x in T:
    print( x )

if "python" in T:
    print("Yes, Python is in languages tuple")

print("Length of the tuple is " , len(T) )
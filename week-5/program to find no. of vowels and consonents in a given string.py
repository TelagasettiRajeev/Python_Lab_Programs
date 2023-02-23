mystr = input("Enter the string : ")

vowel_count = 0
cons_count = 0

for i in mystr:
    if i in { 'a','e','i','o','u','A','E','I','O','U' }:
        vowel_count += 1
    else:
        cons_count += 1
    
print("No. of vowels in " + mystr + " is " + str(vowel_count) )
print("No. of consonents in " + mystr + " is " + str(cons_count) )

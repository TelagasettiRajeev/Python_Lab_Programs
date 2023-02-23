companies = [ 'microsoft' , 'IBM' , 'Accententure' , 'TCS' , 'Delloitte' ]
employes = [ '2,21,000' , '2,82,100' , '17,21,000' , '15,28,748' , '14,15,000' ]

print( "Top Software companies are : " , companies )
print( "Number of employes are : " , employes )

comemp = companies + employes
print( "Companies with employes are : " , comemp )

employes.remove('17,21,000')
print( "Updated employess are : " , employes )
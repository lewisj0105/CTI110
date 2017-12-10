# CTI-110
# M5HW3: Factorial
# Johnny Lewis
# 10/16/2017

userInteger = int( input( "Please enter a number: " ))

while userInteger < 1:
    userInteger = int( input( "Please enter a positive number pleased: " ))

factorial = 1

for currentNumber in range( 1, userInteger + 1 ):
    factorial = factorial * currentNumber

print( "The factorial of", userInteger, "is", factorial )    

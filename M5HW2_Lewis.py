#CT1-110
#M5HW2: Running Total
#Johnny Lewis
#10/16/2017

total = 0
userNumber = float( input( "Please enter the first number or a negative " + \
                           "number to quit: " ))

while userNumber > -1:
    total = total + userNumber
    userNumber = float( input( "Please enter the next number or a " + \
                               "negative number to quit: " ))
print( "The sum of all the number you enter is",total )    




#CT1-110
#M3HW1 - Age Classifier
#Johnny Lewis
#9/22/18

userAge = int( input( "please enter your age: "))

if userAge <= 1:
    print( "you are an infant" )
elif userAge < 13:
    print( "you are an child" )
elif userAge < 20:
    print( "you are a teenager" )
else:
    print( "you are an adult" ) 


# if the person is 1 year old or less, he or she is an infant.
# if the person is older than one year, but younger than 13 years, he or she is a child
# if the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
# if the person is at least 20 years old, he or she is an adult.
    

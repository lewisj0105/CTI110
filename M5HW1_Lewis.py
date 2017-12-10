#CT1-110
#M5HW1: Distance Traveled 

vehicleSpeed = float( input( "what is the speed of the vehical: " ) )
timeTraveled = int( input( "How many hours has it traveled?: " ) )

print()
print( "Hour","\tDistance Travelded" )
for currentHour in range( 1, timeTraveled + 1 ):
    distanceTraveled = vehicleSpeed * currentHour
    print( currentHour,"\t",distanceTraveled)

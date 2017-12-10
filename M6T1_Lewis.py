# CTI - 110
# M6T1 Converter
# Johnny Lewis
# 10/30/2017


def askUserForKilometers():
    userKilometers = float( input( "Please enter the distance" + \
                                   " in Kilometers: " ))
    return userKilometers

def convertKilometersToMiles( userKilometers ):
    miles = userKilometers * 0.6214
    return miles

def main():
    userKilometersTyped = askUserForKilometers()
    convertedMiles = convertKilometersToMiles( userKilometersTyped )

    print( userKilometersTyped, "Kilometers converted to miles is", \
          format( convertedMiles, ".2f" ),"miles" )

main()

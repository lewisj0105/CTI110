# Write a program that asks the user to enter a distance in feet, print that same distance in inches
# 10/31/2017
# CTI-110 M6T2_FeetToInches
# Johnny Lewis

INCHES_PER_FOOT = 12


def main():
    feet = int( input('Enter a distance in feet: '))

    print(feet, 'equals', feet_to_inches(feet), 'inches.')

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT
    
main()

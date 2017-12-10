# write a program that ask user to enter five test grades, display letter grade for each score, and the average test score
# 10/31/2017
# CTI-110 M6HW1 - Test Average and Grade
# Johnny Lewis


def calcAverage( score1, score2, score3, score4, score5 ):
    average = ( score1 + score2 + score3 + score4 + score )/5
    return average

def determineGrade( userScore ):
    if( userScore < 60 ):
        return "F"
    elif( userScore < 70 ):
        return "D"
    elif( userScore < 80 ):
        return "C"
    elif( userScore < 90 ):
        return "B"
    elif( userScore < 101 ):
        return "A"

def askForScores():
    score1 = float( input( "Please enter Score 1: " ))
    score2 = float( input( "Please enter Score 2: " ))
    score3 = float( input( "Please enter Score 3: " ))
    score4 = float( input( "Please enter Score 4: " ))
    score5 = float( input( "Please enter Score 5: " ))

    return score1, score2, score3, score4, score5

def printTableOfResults( score1, score2, score3, score4, score5 ):
    print( "Score\tLetter Grade" )
    print( str( score1 ) + "\t\t" + determineGrade( score1 ), \
           str( score2 ) + "\t\t" + determineGrade( score2 ), \
           str( score3 ) + "\t\t" + determineGrade( score3 ), \
           str( score4 ) + "\t\t" + determineGrade( score4 ), \
           str( score5 ) + "\t\t" + determineGrade( score5 ), sep = "\n" )
           
def main():
    score1, score2, score3, score4, score5 = askForScores()
    print()
    printTableOfResults( score1, score2, score3, score4, score5 )

main()           

# CT1-110
# M3HW2 - SoftwareSales
# Johnny Lewis
# 9/24/2017

userNumberOfPackages = int( input( "please enter the number of pac" + \
                                   "kages bought: "))
packagePrice = 99

if userNumberOfPackages < 10:
    discount = 0;
elif userNumberOfPackages < 20:
    discount = 0.10
elif userNumberOfPackages < 50:
    discount = 0.20
elif userNumberOfPackages < 100:
    discount = 0.30
else:
    discount = 0.40

subTotal = userNumberOfPackages * packagePrice
discountAmount = discount * subTotal
total = subTotal - discountAmount

print( "\nAmount of discount: $" + format( discountAmount, ",.2f" ) + \
       "\nTotal amount: $" + format( total, ",.2f" ))

    

# 3. Software Sales
 
# A software company sells a package that retails for $99. Quantity discounts
# are giving according to the following table:

# Quantity      Discount
# 10-19          10%
# 20-49          20%
# 50-99          30%
# 100 or more    40%

# Write a program that ask the user to enter the number of packages purchased.
# The program should then display the amount of the discount (if any) and the
# total amount of the purchase after the discount.

# Starting out with python. Third Edition. Tony Gaddis.
